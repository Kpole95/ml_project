import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:
    """
    hold the file path where the best model will be saved
    """
    trained_model_file_path=os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            # receives the processed data and split into features "X" and target "y"
            logging.info("Splitting traiing and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
                )
            
            # difiens a dict of models to train
            models={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                # "K-neighbors Classifier": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            # defines a dict of hyperparameters for tuning
            params={
                "Decision Tree": 
                    {#"creterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"],
                    #"splitter":["best", "random"],
                    "max_features":["sqrt", "log2"],
                    },
                "Random Forest":
                    {#"creterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"],
                    #"max_features":['sqrt', 'log2', 'None'],
                    "n_estimators":[8,16,32,64,128,256]
                    },
                "Gradient Boosting":
                    {#"loss": ["squared_error", "huber", "absolute_error", "quantile"],
                    "learning_rate":[.1, .01, .05, .001],
                    "subsample":[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                    },
                "Linear Regression":{},
                "XGBRegressor":
                    {
                    "learning_rate":[.1,.01,.05,.001],
                    "n_estimators":[8,16,32,64,128,256]
                    },
                "CatBoosting Regressor":
                    {
                    "depth":[6,9,10],
                    "learning_rate":[0.01, 0.05, 0.1],
                    "iterations":[30, 50, 100]
                    },
                "AdaBoost Regressor":
                    {
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                    }
                }
            

            # call the evaluation utility to get a performance report
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models, param=params)
            
            # to find the best model score and name from the report (model_report)
            best_model_score= max(sorted(model_report.values()))
            best_model_name= list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            ## check if the best model meet a performance threshold
            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            # save best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # make predictions and return the final score
            predicted=best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
        
        except Exception as e:
            raise CustomException(e, sys)