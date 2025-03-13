import re

class SecretScanner:
    """Scanner that detects exposed secrets in text content."""
    
    def __init__(self):
        # Define patterns for API keys, tokens, passwords, etc.
        self.secret_patterns = [
            r"(?i)[a-z0-9]{5,}-EXPOSED-SECRET-[a-z0-9]{5,}",  # Example: '12345-EXPOSED-SECRET-67890'
            r"ghp_[a-zA-Z0-9]{36}",  # GitHub personal access token (ghp_xxxxx)
            r"(?i)AWS_ACCESS_KEY_ID\s*=\s*['\"]?([A-Z0-9]{20})['\"]?",  # AWS Key
            r"(?i)AWS_SECRET_ACCESS_KEY\s*=\s*['\"]?([A-Za-z0-9/+=]{40})['\"]?",  # AWS Secret Key
        ]

    def scan_text(self, text):
        """Scans the provided text and returns a list of detected secrets."""
        found_secrets = []
        for pattern in self.secret_patterns:
            matches = re.findall(pattern, text)
            if matches:
                found_secrets.extend(matches)
        return found_secrets
