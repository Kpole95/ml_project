import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object   

"""
This script has the logic for taking a new raw data from the web form
and producing a final production. it is the core of the prediction worlflow
"""


class PredictPipeline:
    """
    this class arrange actual prediction by loading the saved artifacts (preprocessor.pkl
    and model.pkl) and using them
    """
    def __init__(self):
        pass
    def predict(self, features):
        try:
            # defines the paths to the saved artifacts
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')

            # laod the objects using the utility function
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")

            # transform the new data using the loaded preprocessor
            data_scaled=preprocessor.transform(features)

            # make prediction using the loaded preprocessor and return
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    """
    this class acts as a blueprit, its job is to take the raw input from the web form
    and structure it correct before it is converted into a formtat the model can understand.
    ## the __Init__ method is called form app.py when receiving the users form inputs.
    """
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int): # takes all the form inputs as arguemebts

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
        # this methods converts the structured data into a pandas dataframe

        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)