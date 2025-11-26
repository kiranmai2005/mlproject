## track events(program started,data loaded etc),errors,diagnostics
##diagnostic(line numbers,timestamps,file names etc).

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="['%(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")

# Configures logging to write into the file at LOG_FILE_PATH.
# Format includes:
# %(asctime)s → timestamp of the log entry
# %(lineno)d → line number where the log was called
# %(name)s → logger name (default is root)
# %(levelname)s → severity (INFO, ERROR, WARNING, etc.)
# %(message)s → actual log message