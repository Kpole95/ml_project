import sys
import os   
from dataclasses import dataclass 
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    """
    to hold the path wjere the final data transformation pipeline will be saved in the **artifacts**
    """
    preprocesser_obj_file_path=os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation: # main logic for the data transformation process
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        """"
        This function is responsible for data transformation
        """
        try:
            
            # defines qhich columns are numericl and which are categorical
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            # create the numerical processing pipeline and handle missin values and scale the data
            num_pipeline= Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())    
                ]
            )

            # create the categorical processing pipeline and handle missing values and convert text to numbers
            cat_pipeline= Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore')),
                # ("scaler", StandardScaler())
                ]
            )
            logging.info("Numberical columns standard scaling completed")
            logging.info("Categorical columns encdoing completed")

            # combines both pipelines in a single preprocessor object
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:

            # received the data paths for data_ingestion step
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and tsst data completed")

            # get the preprocessing objet from the helper method
            logging.info("Obtaiming prrprocessing object")
            preprocessing_obj=self.get_data_transformer_object()
            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]

            # separate the features "X" and Target "y"
            input_feature_train_df=train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df=train_df[target_column_name]
            input_feature_test_df=test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df=test_df[target_column_name]

            ## apply preprocessing pipeline to tje data
            logging.info(
                f"Applyin preprocesing object on training dataframe and testing dataframe."
            )
            input_feature_train_arr =preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr =preprocessing_obj.transform(input_feature_test_df)

            # combine the transformer features and target back in a single array
            train_arr=np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            # save the preprocessor object as a pickle  file
            logging.info("Saved preprocessing objext")
            save_object(
                file_path = self.data_transformation_config.preprocesser_obj_file_path,
                obj=preprocessing_obj
            )

            # return the processed data and preprocesspt path for the next step
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocesser_obj_file_path,
            )
        
        except Exception as e:
            raise CustomException(e, sys)
