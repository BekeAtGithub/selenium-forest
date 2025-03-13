import re  # Import regular expressions for pattern matching

class LogSensitivityScanner:  # Define a class for scanning sensitive data in logs
    def __init__(self):  # Constructor to initialize known sensitive patterns
        self.sensitive_patterns = [
            re.compile(r'(?i)password\s*[=:]\s*"?.{6,}"?'),  # Password pattern
            re.compile(r'(?i)secret\s*[=:]\s*"?.{6,}"?'),  # Secret key pattern
            re.compile(r'(?i)private[_-]?key\s*[=:]\s*"?.{20,}"?'),  # Private key pattern
            re.compile(r'(?i)authorization[: ]\s*"?.+"?'),  # Authorization header pattern
            re.compile(r'(?i)access[_-]?token\s*[=:]\s*"?.{20,}"?')  # Access token pattern
        ]

    def scan_logs(self, log_text):  # Function to scan logs for sensitive information
        """Scan the provided log text and return a list of found sensitive data."""
        found_sensitive_data = []  # Initialize list to store detected sensitive data
        for pattern in self.sensitive_patterns:  # Iterate over known sensitive patterns
            matches = pattern.findall(log_text)  # Search for matches in log text
            if matches:
                found_sensitive_data.extend(matches)  # Add matches to found sensitive data list
        return found_sensitive_data  # Return list of detected sensitive information
