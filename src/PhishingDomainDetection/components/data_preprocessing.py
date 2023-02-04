import os
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE  
from sklearn.preprocessing import StandardScaler  
from PhishingDomainDetection.entity import DataPreprocessConfig
from PhishingDomainDetection import log

class DataPreprocess:
    def __init__(self, config: DataPreprocessConfig):
        self.config = config

    def data_load(self):
        data_path = self.config.load_file_path
        data = pd.read_csv(data_path)
        select_columns = self.config.params_select_columns
        self.df = data[select_columns]
    
    
    def handling_missing_value(self):
        # we have already done research on missing values. you can refer research/preprocessing.ipynb
        # delete params_length because it's having 91% missing values
        self.df = self.df.drop('params_length', axis=1)

        # fill missing values with median
        self.df = self.df.replace(-1, np.nan)
        self.df = self.df.fillna(self.df.median())

    
    def handling_imbalanced_data(self):
        sm = SMOTE(random_state = 33)
        self.df_new, df_phishing_new = sm.fit_resample(self.df.drop('phishing', axis=1), self.df.phishing)
        self.df_new['phishing'] = df_phishing_new

        
   
    def sacling_data(self):
        scaler = StandardScaler()
        self.df_scaled = pd.DataFrame(scaler.fit_transform(self.df_new.drop('phishing', axis=1)),columns = self.df.columns[:-1])
        self.df_scaled['phishing'] = self.df_new.phishing

    
    def saving_preprocessing_data(self):
        data_preprocessing_root_dir = self.config.root_dir
        local_file_dir = self.config.local_file

        raw_local_dir_path = os.path.join(data_preprocessing_root_dir, local_file_dir)

        self.df_scaled.to_csv(raw_local_dir_path, index=False)
