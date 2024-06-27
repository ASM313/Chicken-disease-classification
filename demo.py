from src.cnnClassifier import logger
from src.cnnClassifier.config.configuration import GCloudSync
import sys
from src.cnnClassifier.constants import *

logger.info("Started logging ")

# try:
#     a=1/0

# except Exception as e:
#     raise CustomException(e,sys)
obj = GCloudSync()
obj.sync_folder_from_gcloud(gcp_bucket_url=BUCKET_NAME,filename= ZIP_FILE_NAME, destination="data")