import subprocess
import re
import sys  # Import system functions
import os  # Import OS functions for file handling
import json  # Import JSON for report handling
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget  # Import PyQt GUI components
from PyQt5.QtCore import QThread, pyqtSignal  # Import threading and signals for background tasks

# Ensure `src/` directory and `src/azure_devops_api/` are in Python's import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "azure_devops_api")))

# Import modules from the correct directory structure
from src.azure_devops_api.azure_api_client import AzureAPIClient
from src.azure_devops_api.fetch_builds_azure import FetchBuildsAzure
from src.security_scanner.secret_exposure_scanner import SecretExposureScanner
from src.azure_devops_api.fetch_pipelines_azure import FetchPipelinesAzure
from src.azure_devops_api.fetch_repos_azure import FetchReposAzure
from src.security_scanner.secret_scanner import SecretScanner

# Define directories for logs and reports
LOGS_DIR = "data/logs"
REPORTS_DIR = "data/reports"
REPORT_FILE = os.path.join(REPORTS_DIR, "vulnerability_report.json")

# Ensure necessary directories exist
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

class SeleniumForestApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.scan_threads = {}
        self.scan_results = {}

    def initUI(self):
        self.setWindowTitle("Selenium Forest - Azure DevOps Scanner")
        self.setGeometry(100, 100, 600, 500)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.scan_pipelines_btn = QPushButton("Scan Pipelines", self)
        self.scan_pipelines_btn.clicked.connect(self.scan_pipelines)
        layout.addWidget(self.scan_pipelines_btn)

        self.scan_builds_btn = QPushButton("Scan Build Releases", self)
        self.scan_builds_btn.clicked.connect(self.scan_builds)
        layout.addWidget(self.scan_builds_btn)

        self.scan_repos_btn = QPushButton("Scan Repositories", self)
        self.scan_repos_btn.clicked.connect(self.scan_repositories)
        layout.addWidget(self.scan_repos_btn)

        self.scan_logs_btn = QPushButton("Scan Logs", self)
        self.scan_logs_btn.clicked.connect(self.scan_logs)
        layout.addWidget(self.scan_logs_btn)

        self.export_report_btn = QPushButton("Export Security Report", self)
        self.export_report_btn.clicked.connect(self.export_report)
        layout.addWidget(self.export_report_btn)

        self.run_tests_btn = QPushButton("Run Unittests", self)
        self.run_tests_btn.clicked.connect(self.run_tests)
        layout.addWidget(self.run_tests_btn)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def scan_repositories(self):
        """Trigger PowerShell script to scan for exposed secrets in repositories."""
        print("Scanning Repositories using PowerShell...")

        script_path = os.path.join(os.path.dirname(__file__), "src", "azure_devops_api", "api_scan.ps1")
        log_path = os.path.join(LOGS_DIR, "repository_scan.log")

        try:
            print(f"Running PowerShell script: {script_path}")

            # Execute PowerShell script
            result = subprocess.run(
                ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
                capture_output=True, text=True
            )

            # Log PowerShell output
            with open(log_path, "w", encoding="utf-8") as log:
                log.write(" PowerShell Script Output:\n")
                log.write(result.stdout)
                log.write("\nPowerShell Script Errors:\n")
                log.write(result.stderr)

            print(" PowerShell script executed. Logs saved to:", log_path)

            #  Read the log output & scan for secrets
            with open(log_path, "r", encoding="utf-8") as log:
                scan_output = log.read()

            scanner = SecretExposureScanner()
            found_secrets = scanner.scan_text(scan_output)

            if found_secrets:
                self.scan_results["repositories"] = found_secrets
                print(f" Found exposed secrets in repositories: {found_secrets}")
                self.export_report()

                #  Append found secrets to `repository_scan.log`
                with open(log_path, "a", encoding="utf-8") as log:
                    log.write("\n Detected Secrets:\n")
                    log.write(json.dumps(found_secrets, indent=4))

                print(" Vulnerability report appended to repository_scan.log.")

            else:
                print(" No secrets found in repositories.")

        except Exception as e:
            print(f" Error executing PowerShell script: {e}")

        print(" Repository scan completed.")


    def scan_pipelines(self):
        print(" Scanning Pipelines...")

        client = AzureAPIClient("AzDo Project", "Repo")
        fetcher = FetchPipelinesAzure(client)
        scanner = SecretExposureScanner()

        print("DEBUG: Fetching pipeline data...")
        pipelines = fetcher.get_pipelines()
        print(f"DEBUG: Retrieved Pipelines Data: {pipelines}")

        if not pipelines or "value" not in pipelines:
            print(" No pipelines found or API request failed!")
            return

        detected_vulnerabilities = {}

        for pipeline in pipelines["value"]:
            pipeline_info = str(pipeline)
            print(f"DEBUG: Scanning pipeline {pipeline['id']}...")
            print(f"DEBUG: Pipeline content:\n{pipeline_info[:1000]}")

            found_secrets = scanner.scan_text(pipeline_info)
            print(f"DEBUG: Scanner output -> {found_secrets}")

            if found_secrets:
                detected_vulnerabilities[pipeline["id"]] = found_secrets
                print(f" Found exposed secrets in pipeline {pipeline['id']}: {found_secrets}")
            else:
                print(f" No secrets found in pipeline {pipeline['id']}.")

        if detected_vulnerabilities:
            self.scan_results["pipelines"] = detected_vulnerabilities
            self.export_report()

        print(" Pipeline scan completed.")

    def scan_builds(self):
        """Scan Azure DevOps build logs for exposed secrets."""
        print(" Scanning Build Releases...")

        client = AzureAPIClient("AzDo Project", "Repo")
        fetcher = FetchBuildsAzure(client)
        scanner = SecretExposureScanner()

        print("DEBUG: Fetching build logs...")
        builds = fetcher.get_builds()

        if not builds or "value" not in builds:
            print(" No builds found or API request failed!")
            return

        detected_vulnerabilities = {}

        for build in builds["value"]:
            build_log = str(build)  # Convert the log data to string
            print(f"DEBUG: Scanning build {build['id']} logs...")

            found_secrets = scanner.scan_text(build_log)
            print(f"DEBUG: Scanner output -> {found_secrets}")

            if found_secrets:
                detected_vulnerabilities[build["id"]] = found_secrets
                print(f" Found exposed secrets in build {build['id']}: {found_secrets}")
            else:
                print(f" No secrets found in build {build['id']}.")

        if detected_vulnerabilities:
            self.scan_results["builds"] = detected_vulnerabilities
            self.export_report()

        print(" Build scan completed.")


    def scan_logs(self):
        """Scan local log files for sensitive data using the improved scanner."""
        print(" Scanning Logs...")

        scanner = SecretScanner()
        if not os.path.exists(LOGS_DIR):
            print(f" Logs directory not found: {LOGS_DIR}")
            return

        detected_vulnerabilities = {}

        for log_file in os.listdir(LOGS_DIR):
            log_path = os.path.join(LOGS_DIR, log_file)
            if not os.path.isfile(log_path):
                continue  

            print(f"DEBUG: Scanning log file: {log_file}")

            with open(log_path, "r", encoding="utf-8") as file:
                log_content = file.read()

            found_secrets = scanner.scan_text(log_content)
            print(f"DEBUG: Scanner output -> {found_secrets}")

            if found_secrets:
                detected_vulnerabilities[log_file] = found_secrets
                print(f" Found exposed secrets in {log_file}: {found_secrets}")
            else:
                print(f" No secrets found in {log_file}.")

        if detected_vulnerabilities:
            self.scan_results["logs"] = detected_vulnerabilities
            self.export_report()

        print(" Log scan completed.")

    def export_report(self):
        print("Exporting security report...")
        with open(REPORT_FILE, "w") as report:
            json.dump(self.scan_results, report, indent=4)
        print(f"Report successfully exported to {REPORT_FILE}")

    def run_tests(self):
        print("Running unit tests...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = SeleniumForestApp()
    mainWin.show()
    sys.exit(app.exec_())
