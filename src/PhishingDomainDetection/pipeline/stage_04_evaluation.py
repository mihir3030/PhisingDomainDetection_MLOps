from PhishingDomainDetection.config import ConfigurationManager
from PhishingDomainDetection.components import Evaluation
from PhishingDomainDetection import log

STAGE_NAME = "Evaluation Stage"
def main():
    config = ConfigurationManager()
    evaluation_config = config.get_evaluation_config()
    evaluation = Evaluation(config=evaluation_config)
    evaluation.load_test_data()
    evaluation.load_model()
    evaluation.evaluation()
    evaluation.save_score()

if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>{STAGE_NAME} started")
        main()
        log.info(f">>>>>>>>>>{STAGE_NAME} compleated successfully\n\n X==========================X\n\n")
    except Exception as e:
        log.exception(e)
        raise e