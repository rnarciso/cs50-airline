import logging

# Create and configure a logger
LOG_FILE = "C:\\Users\\Hosam\\Desktop\\logger.log"
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(LeveLname)s %(asctime)s - %(message)s"
LOG_MODE = 'w'
logging.basicConfig(filename=LOG_FILE,
                    level=LOG_LEVEL,
                    format=LOG_FORMAT,
                    filemode=LOG_MODE)
logger = logging.getLogger()

# Test the logger
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("his is an error message.")
logger.critical("This is a critical error message.")
