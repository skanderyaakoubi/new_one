import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


from src.exception import CustomException
from src.logger import logging 



class DataTransformationConfig :
    preprocessor_obj_file_path=os.path.join("artifactss","preprocessor.pkl")


class DataTransformation:
    def __init__(self) :
        self.data_transformation_config=DataTransformationConfig()
    def get_data_transformer(self):
        try :
            numerical_columns=["writing_score","reading_score"]
            categorical_columns=["gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course"]
            num_pipeline= Pipeline(
                steps={
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())

                    }

            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent"))
                    ("one_hot_encoder",OneHotEncoder())
                ]
            )
            logging.info("numerical & categorical completed")

            preprocessor=
        except:
            pass


