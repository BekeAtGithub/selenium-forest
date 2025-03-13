import unittest  # Import unittest for test cases
from ai_llm_analyzer import LLMVulnerabilityAnalyzer  # Import the AI vulnerability analyzer

class TestAIAnalysis(unittest.TestCase):  # Define a test case for AI analysis
    def setUp(self):  # Setup function to initialize the analyzer
        self.analyzer = LLMVulnerabilityAnalyzer()  # Instantiate AI analyzer

    def test_analyze_text(self):  # Test function to validate AI analysis
        sample_text = "This is a test with a potential secret: API_KEY=12345abcd"  # Sample input
        result = self.analyzer.analyze_text(sample_text)  # Run analysis
        self.assertIsInstance(result, str)  # Assert that result is a string
        self.assertGreater(len(result), 0)  # Ensure result is not empty

if __name__ == "__main__":  # Main entry point for running tests
    unittest.main()  # Execute tests
