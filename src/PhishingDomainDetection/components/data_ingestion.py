import os
import pandas as pd
import io
import requests
from PhishingDomainDetection.entity import DataIngestionConfig
from PhishingDomainDetection import log

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self,):
        url = self.config.source_URL
        log.info(f"dataset downloading from {url}")
        url_data = requests.get(url).content
        self.df = pd.read_csv(io.StringIO(url_data.decode('-utf-8')))
        log.info(f"dataset download successfully from {url}")
        return self.df

    def save_data(self):
        data_ingestion_root_dir = self.config.root_dir
        local_file_dir = self.config.local_file

        raw_local_dir_path = os.path.join(data_ingestion_root_dir, local_file_dir)

        self.df.to_csv(raw_local_dir_path, index=False)
        log.info(f"data saved successfully at {raw_local_dir_path}")