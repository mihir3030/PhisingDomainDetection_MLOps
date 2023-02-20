from PhishingDomainDetection.config import ConfigurationManager
from PhishingDomainDetection.components import DataPreprocess
from PhishingDomainDetection import log

STAGE_NAME = "Data Preprocessing Stage"
def main():
    config = ConfigurationManager()
    data_preprocess_config = config.get_data_preprocess_config()
    data_preprocess = DataPreprocess(config=data_preprocess_config)
    data_preprocess.data_load()
    data_preprocess.handling_missing_value()
    data_preprocess.handling_imbalanced_data()
    data_preprocess.sacling_data()
    data_preprocess.saving_preprocessing_data()


if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>{STAGE_NAME} started")
        main()
        log.info(f">>>>>>>>>>{STAGE_NAME} compleated successfully\n\n X==========================X\n\n")
    except Exception as e:
        log.exception(e)
        raise e