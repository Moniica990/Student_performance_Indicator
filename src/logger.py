import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
# create a folder + log file path so your program can save logs in an organized way
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ]  %(lineno)d  %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

    )


# to check the working of the file
# if __name__=="__main__":
#     logging.info("Logging has started")
    





# your_project/
#   └── logs/
#         └── 04_16_2026_14_30_10.log