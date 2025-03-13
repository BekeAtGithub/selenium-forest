import yaml  # Import YAML for configuration parsing

class ConfigLoaderUtil:  # Define a class to handle config file loading
    def __init__(self, config_path="config.yaml"):  # Constructor with default config path
        self.config_path = config_path  # Store config file path
        self.config_data = self.load_config()  # Load config on initialization

    def load_config(self):  # Function to load YAML config file
        """Load configuration settings from a YAML file."""
        try:
            with open(self.config_path, "r") as file:  # Open the config file in read mode
                return yaml.safe_load(file)  # Load YAML data safely
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {self.config_path} not found.")  # Handle missing file error
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML configuration: {str(e)}")  # Handle YAML parsing errors

    def get_setting(self, key, default=None):  # Function to retrieve config values
        """Retrieve a setting value from the config data."""
        return self.config_data.get(key, default)  # Return the value or default if key is missing
