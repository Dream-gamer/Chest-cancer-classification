from chestCancerClassifier.config.configuration import ConfigurationManager
from chestCancerClassifier.components.model_evaluation_mlfow import Evaluation
from chestCancerClassifier import logger


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()



if __name__ =="__main":
    try:
        logger.info(f"********************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e