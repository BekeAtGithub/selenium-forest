import os  # Import os for environment variable handling
from dotenv import load_dotenv  # Import dotenv for loading environment variables

def setup_environment():  # Function to set up environment variables
    """Load environment variables from .env file."""
    load_dotenv()  # Load variables from .env file
    
    required_vars = ["AZURE_DEVOPS_PAT", "OPENAI_API_KEY"]  # List of required environment variables
    
    for var in required_vars:  # Iterate over required variables
        if not os.getenv(var):  # Check if variable is set
            raise ValueError(f"Missing required environment variable: {var}")  # Raise error if missing

if __name__ == "__main__":  # Main entry point for script execution
    try:
        setup_environment()  # Call environment setup function
        print("Environment variables successfully loaded.")  # Print success message
    except ValueError as e:
        print(f"Error: {e}")  # Print error message if variables are missing
