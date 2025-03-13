from azure_api_client import AzureAPIClient  # Import the Azure API client

class FetchPipelinesAzure:
    def __init__(self, client: AzureAPIClient):
        self.client = client

    def get_pipelines(self):
        """Fetch pipeline details from Azure DevOps"""
        endpoint = "pipelines"
        print(f"DEBUG: Making API request to fetch pipelines: {endpoint}")  # Debugging API call
        response = self.client.make_request(endpoint)

        print(f"DEBUG: Raw API response for pipelines: {response}")  # Debug API response

        if isinstance(response, str):
            print(f"API request failed: {response}")
            return {"value": []}  # Prevent crashing by returning an empty list

        return response

