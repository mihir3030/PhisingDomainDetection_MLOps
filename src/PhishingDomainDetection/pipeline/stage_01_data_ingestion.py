from PhishingDomainDetection.config import ConfigurationManager
from PhishingDomainDetection.components import DataIngestion
from PhishingDomainDetection import log

STAGE_NAME = "Data Ingestion Stage"
def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.save_data()




if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>{STAGE_NAME} started")
        main()
        log.info(f">>>>>>>>>>{STAGE_NAME} compleated successfully\n\n X==========================X\n\n")
    except Exception as e:
        log.exception(e)
        raise e