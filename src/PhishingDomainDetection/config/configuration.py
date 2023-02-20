from PhishingDomainDetection.constants import CONFIG_FILE_PATH, PARAMS_FILE_APTH
from PhishingDomainDetection.utils import read_yaml_file, create_directories
from PhishingDomainDetection import log
from pathlib import Path
import os
from PhishingDomainDetection.entity import DataIngestionConfig, DataPreprocessConfig, TrainingConfig, EvaluationConfig

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
       

    def get_data_preprocess_config(self) -> DataPreprocessConfig:
        data_preprocessing = self.config.data_preprocessing
        dataset_load = os.path.join(self.config.data_ingestion.root_dir, self.config.data_ingestion.local_file) 
        create_directories([data_preprocessing.root_dir])

        data_preprocess_config = DataPreprocessConfig(
            root_dir=Path(data_preprocessing.root_dir),
            load_file_path=Path(dataset_load),
            local_file=Path(data_preprocessing.local_file),
            params_select_columns=self.params.select_columns
        )

        return data_preprocess_config
       

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        dataset_load = os.path.join(self.config.data_preprocessing.root_dir, self.config.data_preprocessing.local_file)

        create_directories([training.root_dir])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            load_file_path=Path(dataset_load),
            test_data_save=Path(training.test_data_save),
            model_save=Path(training.model_save)
        )

        return training_config


    def get_evaluation_config(self) -> EvaluationConfig:
        evaluation = self.config.model_evaluation
        load_model = os.path.join(self.config.training.root_dir, self.config.training.model_save)
        load_test_data = os.path.join(self.config.training.root_dir, self.config.training.test_data_save)

        create_directories([evaluation.root_dir])

        evaluation_config = EvaluationConfig(
            root_dir=Path(evaluation.root_dir),
            load_model_path=Path(load_model),
            load_test_data=Path(load_test_data),
            local_file=Path(evaluation.local_file)
        )
        
        return evaluation_config