from azure_api_client import AzureAPIClient  # Import the Azure API client

import subprocess
import os

class FetchReposAzure:
    def __init__(self):
        """Initialize repository fetcher"""
        self.script_path = os.path.join(os.path.dirname(__file__), "api_scan.ps1")
        self.log_file = os.path.join(os.path.dirname(__file__), "../data/logs/api_scan.log")

    def run_powershell_scan(self):
        """Run PowerShell script and log output"""
        try:
            print(f"Running PowerShell script: {self.script_path}")

            # Execute PowerShell script
            result = subprocess.run(
                ["powershell", "-ExecutionPolicy", "Bypass", "-File", self.script_path],
                capture_output=True, text=True
            )

            # Log PowerShell output
            with open(self.log_file, "w", encoding="utf-8") as log:
                log.write(" PowerShell Script Output:\n")
                log.write(result.stdout)
                log.write("\n PowerShell Script Errors:\n")
                log.write(result.stderr)

            print(" PowerShell script executed. Logs saved to:", self.log_file)

            # Return stdout from PowerShell
            return result.stdout

        except Exception as e:
            print(f" Error executing PowerShell script: {e}")
            return None


