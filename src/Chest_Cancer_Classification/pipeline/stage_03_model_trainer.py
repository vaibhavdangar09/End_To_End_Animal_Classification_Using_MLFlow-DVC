from Chest_Cancer_Classification.config.configuraton import ConfigurationManager
from Chest_Cancer_Classification.components.model_trainer import Training
from Chest_Cancer_Classification import logger

STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self) :
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == '__main__':
    try:
        logger.info(f"****************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e 
