from PhishingDomainDetection.constants import CONFIG_FILE_PATH, PARAMS_FILE_APTH
from PhishingDomainDetection.utils import read_yaml_file, create_directories
from PhishingDomainDetection import log
from pathlib import Path
import os
from PhishingDomainDetection.entity import DataIngestionConfig, DataPreprocessConfig

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_APTH):
        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_file=Path(config.local_file)
        )

        return data_ingestion_config

    def get_data_load_for_preprocess(self):
        self.data_load_config = self.config.data_ingestion
        self.root_dir = self.data_load_config.root_dir
        self.file_dir = self.data_load_config.local_file
        self.file_path = os.path.join(self.root_dir, self.file_dir)
        return self.file_path
       

    def get_data_preprocess_config(self) -> DataPreprocessConfig:
        config = self.config.data_preprocessing
        create_directories([config.root_dir])
        data_preprocess_config = DataPreprocessConfig(
            root_dir=Path(config.root_dir),
            load_file_path=Path(self.get_data_load_for_preprocess()),
            local_file=Path(config.local_file),
            params_select_columns=self.params.select_columns
        )

        return data_preprocess_config