import unittest  # Import unittest for test cases
from unittest.mock import patch, MagicMock  # Import patch and MagicMock for mocking API calls
from azure_api_client import AzureAPIClient  # Import the Azure API client

class TestAzureAPI(unittest.TestCase):  # Define a test case for Azure API interactions
    def setUp(self):  # Setup function to initialize Azure API client
        self.client = AzureAPIClient("test-org", "test-project")  # Instantiate API client with test values

    @patch("azure_api_client.requests.get")  # Mock requests.get for API calls
    def test_make_request(self, mock_get):  # Test function for making API requests
        mock_response = MagicMock()  # Create a mock response object
        mock_response.status_code = 200  # Set status code to 200 OK
        mock_response.json.return_value = {"value": ["test_data"]}  # Mock JSON response
        mock_get.return_value = mock_response  # Assign mock response to get request
        
        result = self.client.make_request("pipelines")  # Make a test API request
        self.assertEqual(result, {"value": ["test_data"]})  # Assert expected response

if __name__ == "__main__":  # Main entry point for running tests
    unittest.main()  # Execute tests
