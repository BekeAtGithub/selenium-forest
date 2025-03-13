from src.azure_devops_api.azure_api_client import AzureAPIClient

class FetchBuildsAzure:
    def __init__(self, client: AzureAPIClient):
        self.client = client

    def get_builds(self):
        """Fetch build logs from Azure DevOps"""
        endpoint = "build/builds"
        response = self.client.make_request(endpoint)

        # Debugging: Print the raw API response
        print("DEBUG: Raw API response:", response)

        # Ensure we handle errors properly
        if isinstance(response, str):
            print("API request failed:", response)
            return {"value": []}  # Return an empty list instead of crashing

        return response
