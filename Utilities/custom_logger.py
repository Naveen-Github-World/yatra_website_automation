import logging
import os
from logging.handlers import RotatingFileHandler

class LogGeneration:
    @staticmethod
    def loggen():
        """ Creating a log file name and log format"""
        try:
            log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Logs')
            log_file = os.path.join(log_directory, 'automation.log')

            # Ensure the directory exists
            os.makedirs(log_directory, exist_ok=True)

            # Create logger
            logger = logging.getLogger('YatraAutomation')
            logger.setLevel(logging.INFO)

            # Check if logger already has handlers to avoid duplicate logs
            if not logger.handlers:
                # Create formatter
                formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                              datefmt='%m/%d/%Y %I:%M:%S %p')

                # File Handler
                file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=2)
                file_handler.setLevel(logging.INFO)
                file_handler.setFormatter(formatter)

                # Console Handler
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)
                console_handler.setFormatter(formatter)

                # Add handlers to logger
                logger.addHandler(file_handler)
                logger.addHandler(console_handler)

            logger.info("Logging initialized successfully")
            return logger
        except Exception as e:
            print(f"Error initializing logger: {str(e)}")
            return None