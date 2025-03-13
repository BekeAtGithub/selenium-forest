import os
import base64
from dotenv import load_dotenv  # Import dotenv to load secrets

# Load environment variables from .env
load_dotenv()

class AzureAPIAuthUtil:
    def __init__(self):
        self.pat = os.getenv("AZURE_DEVOPS_PAT")  # Load PAT from environment
        if not self.pat:
            raise ValueError("Azure DevOps PAT is missing. Set AZURE_DEVOPS_PAT in .env or pipeline.")

    def get_auth_header(self):
        """Generate the authentication header for Azure DevOps API requests."""
        auth_bytes = f":{self.pat}".encode("utf-8")  # Encode PAT
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")  # Convert to Base64
        return {"Authorization": f"Basic {auth_base64}"}  # Return auth header
