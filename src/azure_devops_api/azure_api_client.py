import os
import base64
from dotenv import load_dotenv  # Import dotenv to load environment variables
import requests  # Import requests for API calls
import certifi


# Load environment variables from .env
load_dotenv()

class AzureAPIClient:
    def __init__(self, organization, project):
        self.organization = organization
        self.project = project
        self.pat = ""  # your PAT here

        if not self.pat:
            raise ValueError(" Azure DevOps PAT is missing. Set AZURE_DEVOPS_PAT in a .env file or as an environment variable.")

        # Encode PAT correctly for authentication
        encoded_pat = base64.b64encode(f":{self.pat}".encode()).decode()

        self.base_url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {encoded_pat}"  # Correctly encoded PAT
        }

    def make_request(self, endpoint):
        """Function to make GET requests to Azure DevOps API."""
        
        if "api-version=" not in endpoint:  # Ensure `api-version` is added only once
            endpoint += "?api-version=6.0"
    
        url = f"{self.base_url}/{endpoint}"  # Ensure correct URL formatting
    
        print(f"DEBUG: Making API request to {url}")  # Debugging Step
    
        try:
            response = requests.get(url, headers=self.headers, verify=False)  # Disable SSL warnings (Optional)
            response.raise_for_status()  # Raise error if request fails
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as req_error:
            print(f"API request failed: {req_error}")
            return f"Error fetching data: {req_error}"
    
    
