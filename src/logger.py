import logging
import os
from datetime import datetime

"""
This script configures a logging system to record all the important events, info messages
and errors as a timestamped file for each run of the application
"""

# creates a unique lof file name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# path for the 'logs'dir and creates ot
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# create full path to specific log files
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


# configure the loggin system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)