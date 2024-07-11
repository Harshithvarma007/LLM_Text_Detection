from LLM_text_detection.components.Model_evaluation import *
from LLM_text_detection.config.configuration import ConfigurationManager
STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self,res):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.eval(res[1],res[3])



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
