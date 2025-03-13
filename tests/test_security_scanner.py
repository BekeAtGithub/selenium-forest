import unittest  # Import unittest for test cases
from scanner_secret_exposure import SecretExposureScanner  # Import the secret scanner

class TestSecurityScanner(unittest.TestCase):  # Define test case for security scanning
    def setUp(self):  # Setup function to initialize scanner
        self.scanner = SecretExposureScanner()  # Instantiate secret scanner

    def test_scan_text(self):  # Test function for scanning text
        sample_text = "This contains a password: password=supersecret"  # Sample input with a password
        results = self.scanner.scan_text(sample_text)  # Run scan
        self.assertGreater(len(results), 0)  # Ensure at least one result is found
        self.assertIn("password=supersecret", results)  # Check if detected text is in results

if __name__ == "__main__":  # Main entry point for running tests
    unittest.main()  # Execute tests
