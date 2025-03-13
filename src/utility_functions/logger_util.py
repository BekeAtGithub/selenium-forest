import logging  # Import Python's built-in logging module

class LoggerUtil:  # Define a class for handling logging
    def __init__(self, log_file="data/logs/selenium_forest.log", log_level=logging.INFO):  # Constructor to initialize logger
        self.logger = logging.getLogger("SeleniumForestLogger")  # Create logger instance
        self.logger.setLevel(log_level)  # Set logging level
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)  # Define log file handler
        file_handler.setLevel(log_level)  # Set logging level for file
        
        # Create console handler
        console_handler = logging.StreamHandler()  # Define console log handler
        console_handler.setLevel(log_level)  # Set logging level for console
        
        # Define log message format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Define log message format
        file_handler.setFormatter(formatter)  # Apply formatter to file handler
        console_handler.setFormatter(formatter)  # Apply formatter to console handler
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)  # Attach file handler to logger
        self.logger.addHandler(console_handler)  # Attach console handler to logger
    
    def get_logger(self):  # Function to return the logger instance
        return self.logger  # Return configured logger instance
