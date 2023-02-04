from PhishingDomainDetection.constants import CONFIG_FILE_PATH, PARAMS_FILE_APTH
from PhishingDomainDetection.utils import read_yaml_file, create_directories
from PhishingDomainDetection import log
from pathlib import Path
from PhishingDomainDetection.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config = read_yaml_file(config_file_path)
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