import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    """
    Hold the file paths for training, test and a copy of raw data
    and save them in the *artifacts folder*
    """
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    """
    
    """
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        
        """
        logging.info("Entered the data ingestion method or component")
        try:
            # read the dataset
            df = pd.read_csv(os.path.join("notebook", "data", "stud.csv"))
            logging.info('Read the dataset as dataframe')
            
            # create artfacts dir if it do not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            # save the raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # this will perform train test split
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            # save train test split
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Inmgestion of the data iss completed")

            # return the paths for next step
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":

    # start data ingestion
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    # start data transform
    data_transformation=DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    logging.info("Data transformation complete.")

    # start model training
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))