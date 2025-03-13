import re

class SecretExposureScanner:
    def __init__(self):
        #  Improve regex for detecting API keys & sensitive data
        self.secret_patterns = [
            re.compile(r'API_KEY\s*=\s*["\']([A-Za-z0-9\-_]+)["\']', re.IGNORECASE),
            re.compile(r'AKIA[0-9A-Z]{16}', re.IGNORECASE),  # AWS Key example
            re.compile(r'ghp_[A-Za-z0-9]{36}', re.IGNORECASE),  # GitHub Token
            re.compile(r'eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+', re.IGNORECASE),  # JWT
        ]

    def scan_text(self, text):
        """Scan text for secret exposures."""
        print("DEBUG: Scanning text for secrets...")
        found_secrets = []

        #  Split text into lines to check secrets across multiple lines
        lines = text.split("\n")
        for i, line in enumerate(lines):
            for pattern in self.secret_patterns:
                matches = pattern.findall(line)
                if matches:
                    print(f" !!!!!!! Found secrets in line {i+1}: {matches} !!!!!!!!")
                    found_secrets.extend(matches)

        return found_secrets
