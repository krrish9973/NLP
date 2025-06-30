from hate.configuration.gcloud_syncer import GCloudSync
from hate.entity.config_entity import DataIngestionConfig

x = DataIngestionConfig()
gcloud = GCloudSync()
gcloud.sync_folder_from_gcloud(x.BUCKET_NAME,x.ZIP_FILE_NAME,"dayas")
