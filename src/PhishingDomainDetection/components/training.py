import pandas as pd
import numpy as np
import os
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split      
from sklearn.preprocessing import StandardScaler  
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from PhishingDomainDetection.entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def load_data(self):
        data_path = self.config.load_file_path
        self.df = pd.read_csv(data_path)

    def spliting_data(self):
        self.train, test = train_test_split(self.df, test_size=0.3, random_state=33)
        training_root_dir = self.config.root_dir
        local_file_dir = self.config.test_data_save
        raw_local_dir_path = os.path.join(training_root_dir, local_file_dir)
        test.to_csv(raw_local_dir_path, index=False)

    def model_training(self):
        x = self.train.drop("phishing", axis=1)
        y = self.train['phishing']
        
        self.random_forest = RandomForestClassifier(max_depth=18, max_features='sqrt', min_samples_leaf=2, n_estimators=200)
        self.random_forest.fit(x, y)

    def save_model(self):
        training_root_dir = self.config.root_dir
        model_file_dir = self.config.model_save

        raw_model_file_path = os.path.join(training_root_dir, model_file_dir)
        joblib.dump(self.random_forest, raw_model_file_path)

