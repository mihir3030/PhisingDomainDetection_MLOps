from PhishingDomainDetection.config import ConfigurationManager
from PhishingDomainDetection.components import Training
from PhishingDomainDetection import log

STAGE_NAME = "Training Stage"
def main():
    config = ConfigurationManager()
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.load_data()
    training.spliting_data()
    training.model_training()
    training.save_model()

if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>{STAGE_NAME} started")
        main()
        log.info(f">>>>>>>>>>{STAGE_NAME} compleated successfully\n\n X==========================X\n\n")
    except Exception as e:
        log.exception(e)
        raise e