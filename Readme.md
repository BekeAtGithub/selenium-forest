# SOURCE DOCUMENTATION USED TO BUILD APPLICATION;


### **Azure DevOps API & Git Repositories**
- **Azure DevOps REST API Reference**:  
  -- [https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1)  
  _(Comprehensive reference on Azure DevOps REST APIs)_

- **Azure Repositories REST API**:  
  -- [https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories)  
  _(How to interact with Git repos in Azure DevOps via API)_

- **Azure DevOps Security and Permissions**:  
  -- [https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access)  
  _(Understanding access control and permissions for API authentication)_

### **PowerShell Scripting & Automation**
- **PowerShell Invoke-RestMethod** (Used to interact with the API):  
  -- [https://learn.microsoft.com/en-us/powershell/scripting/samples/rest-api-invoke-restmethod](https://learn.microsoft.com/en-us/powershell/scripting/samples/rest-api-invoke-restmethod)  

- **PowerShell Execution Policies** (For running scripts without issues):  
  -- [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy)  

### **Python & Security Scanning**
- **Python Subprocess (Used to trigger PowerShell scripts from Python)**:  
  -- [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)  

- **Logging in Python (For Writing Logs to Files)**:  
  -- [https://docs.python.org/3/library/logging.html](https://docs.python.org/3/library/logging.html)  

- **Regular Expressions (`re` module for Secret Scanning)**:  
  -- [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)  

### **PyQt GUI Development**
- **PyQt5 Official Documentation**:  
  -- [https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)  

- **PyQt5 Signals and Slots (Used for threading & background tasks)**:  
  -- [https://doc.qt.io/qtforpython-6/PySide6/QtCore/QThread.html](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QThread.html)  

### **JSON & Report Handling**
- **Working with JSON in Python**:  
  -- [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)  

---

Here are some public GitHub repositories and resources that offer similar functionalities :

1. **ADOScanner**: This repository provides a security scanner specifically designed for Azure DevOps (ADO). It focuses on assessing the security posture of ADO environments.

   - GitHub Repository: https://github.com/azsk/ADOScanner


2. **GitHub Advanced Security for Azure DevOps**: GitHub offers an advanced security suite that integrates with Azure DevOps, providing features like code scanning, secret scanning, and dependency scanning.

   - Overview: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
   

3. **Code Scanning with CodeQL**: GitHub's CodeQL is a powerful semantic code analysis engine that can identify vulnerabilities across various codebases. It can be integrated into Azure DevOps pipelines for enhanced security scanning.

   - Documentation: https://resources.github.com/security/github-advanced-security-for-azure-devops/?utm_source=chatgpt.com
   https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-code-scanning?view=azure-devops


These resources should provide valuable insights and tools to enhance the security scanning capabilities within Azure DevOps environments. 


# Selenium Forest - Azure DevOps Vulnerability Scanner

Selenium Forest is a security tool that scans Azure DevOps pipelines, builds, repositories, and logs for exposed secrets and vulnerabilities using AI-powered analysis.

## Setup Guide (From Scratch)

This guide will walk you through the setup process from the ground up. No prior installations or configurations are assumed.

---

## 1 Install Required Software

Before running the scanner, install the necessary tools.

###  Step 1: Install Python (If Not Installed)
Selenium Forest requires **Python 3.8+**.

- **Windows**:
  1. Download Python from [python.org](https://www.python.org/downloads/)
  2. Run the installer and check **"Add Python to PATH"** before installing.

- **Mac/Linux**:
  ```sh
  sudo apt update && sudo apt install python3 python3-pip -y  # Ubuntu/Debian
  brew install python  # macOS (if using Homebrew)
  ```

Verify installation:
```sh
python3 --version
```

---

## 2 Clone the Repository

Use Git to download the project.
```sh
git clone https://github.com/your-repo/selenium-forest.git
cd selenium-forest
```

If you don’t have Git installed:
- **Windows**: Download [Git](https://git-scm.com/downloads) and install it.
- **Mac/Linux**:
  ```sh
  sudo apt install git -y  # Ubuntu/Debian
  brew install git  # macOS
  ```

---

## 3 Create a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

---

## 4 Install Dependencies

```sh
pip install -r requirements.txt
```

If you don’t have `pip`:
```sh
python3 -m ensurepip --default-pip
```

---

## 5 Configure Environment Variables

Create a **`.env`** file in the project root and add:
```sh
AZURE_DEVOPS_PAT=your_personal_access_token
OPENAI_API_KEY=your_openai_api_key
```
**Replace values** with your actual credentials.

---

## 6 Set Up Configuration File

Edit **`config.yaml`** to match your Azure DevOps organization and project:
```yaml
azure_devops:
  organization: "your-org-name"
  project: "your-project-name"
  personal_access_token: "${AZURE_DEVOPS_PAT}"
```

---

## 7 Run the Scanner

Run the vulnerability scanner:
```sh
python scripts/run_vulnerability_scanner.py
```

---

## 8 View the Scan Results

Reports are stored in:
```sh
data/reports/vulnerability_report.json
```
To view results:
```sh
cat data/reports/vulnerability_report.json
```

---

## 9 Launch the GUI

Run the GUI for manual scanning:
```sh
python selenium_forest.py
```

Click the buttons to scan different Azure DevOps components.

---

## Additional Commands

### Export a Report
```sh
python scripts/export_security_report.py
```

### Run Tests
```sh
python -m unittest discover tests/
```

---

## Troubleshooting

🔹 **Python Not Found?** Try `python3` instead of `python`.
🔹 **Permission Denied?** Add `sudo` before commands (Linux/macOS).
🔹 **Missing Dependencies?** Run `pip install -r requirements.txt` again.
🔹 **Invalid API Key?** Ensure `OPENAI_API_KEY` and `AZURE_DEVOPS_PAT` are correct.

---


---

### **azure-devops-vuln-scanner/**
```
selenium-forest/
│── selenium_forest.py         # Main entry point for GUI
│── requirements.txt           # Dependencies (Selenium, OpenAI, LlamaIndex, PyQt/Tkinter, etc.)
│── config.yaml                # Configuration file (API keys, Azure DevOps org, project names)
│── README.md                  # Documentation for setup and usage
│
├── data/                      # Data storage (logs, cached results)
│   ├── logs/                  # Store scanning logs
│   ├── reports/               # Generated security reports
│
├── src/                       
│   ├── gui_components/        # GUI Components
│   │   ├── main_window_gui.py  # Main GUI window
│   │   ├── results_display_gui.py  # Results display window
│   │   ├── gui_styles.py       # GUI styling (if using PyQt)
│
│   ├── ai_analysis/           # AI Components
│   │   ├── llm_vulnerability_analyzer.py  # Uses LlamaIndex/OpenAI for secret detection
│   │   ├── prompt_templates_ai.py  # Prompt engineering for AI-based scanning
│
│   ├── azure_devops_api/      # Azure DevOps API interactions
│   │   ├── api_scan.ps1        # some policies will block Python API calls to read certain files, so powershell is an alternative
│   │   ├── azure_api_client.py   # API Client for Azure DevOps
│   │   ├── fetch_pipelines_azure.py  # Fetch pipeline details
│   │   ├── fetch_builds_azure.py  # Fetch build releases and logs
│   │   ├── fetch_repos_azure.py  # Fetch repo files for scanning
│
│   ├── security_scanner/      # Vulnerability Scanner
│   │   ├── secret_exposure_scanner.py  # Checks for exposed secrets
│   │   ├── log_sensitivity_scanner.py  # Scans logs for sensitive data
│   │   ├── code_vulnerability_scanner.py  # Scans repo files for vulnerabilities
│
│   ├── utility_functions/     # Helper functions
│   │   ├── config_loader_util.py  # Loads config.yaml
│   │   ├── logger_util.py  # Custom logger setup
│   │   ├── azure_api_auth_util.py  # Azure DevOps authentication helpers
│
├── tests/                     # Unit and integration tests
│   ├── test_ai_analysis.py  # Tests AI analysis
│   ├── test_azure_api.py  # Tests Azure DevOps API client
│   ├── test_security_scanner.py  # Tests vulnerability scanner
│
└── scripts/                   # Utility scripts
    ├── setup_environment.py  # Initial setup script (API key setup)
    ├── run_vulnerability_scanner.py  # CLI-based scanner execution
    ├── export_security_report.py  # Exports scanning results as a report
```

---

Key Features of this Structure
Azure DevOps API Client (azure_devops_api/): Fetches data from pipelines, builds, logs, and repositories.
AI Analysis (ai_analysis/): Uses OpenAI/LlamaIndex to analyze logs, pipeline scripts, and code.
Secret & Log Scanning (security_scanner/): Checks for API keys, passwords, tokens, and other sensitive data.
GUI (gui_components/): Built using PyQt5 or Tkinter to allow manual execution of scans.
Config & Logging (config.yaml and utility_functions/): Stores API keys and logging setup.
Automated Testing (tests/): Ensures reliability of scanning logic and API interactions.

---


### **Next Steps**
Since everything is working now, here are some things you might want to explore next:
- Automating Azure DevOps security checks in **GitHub Actions**: [https://learn.microsoft.com/en-us/azure/devops/pipelines/integrations/github](https://learn.microsoft.com/en-us/azure/devops/pipelines/integrations/github)
- Enhancing **secret scanning with `truffleHog`**: [https://github.com/trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)
- Packaging this as a **CLI tool or Flask API** for better usability.
