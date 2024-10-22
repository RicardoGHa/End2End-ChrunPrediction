import os  # Module to interact with the operating system
import sys  # Module to access system-specific parameters and functions
import logging  # Module for logging messages and events

# Define the format for log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory where log files will be saved
log_dir = "logs"

# Full file path for the log file inside the 'logs' directory
log_filepath = os.path.join(log_dir, "running_log.log")

# Create the directory for log files if it doesn't exist already
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level to INFO (logs INFO, WARNING, ERROR, CRITICAL)
    format=logging_str,  # Define the format for log messages
    handlers=[  # List of handlers where logs will be sent
        logging.FileHandler(
            log_filepath
        ),  # Logs will be saved to 'running_log.log' file
        logging.StreamHandler(
            sys.stdout
        ),  # Logs will also be displayed on the console (stdout)
    ],
)

# Create a logger object named 'mlProjectLogger'
logger = logging.getLogger("mlProjectLogger")
