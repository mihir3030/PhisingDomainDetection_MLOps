import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, f1_score
import pandas as pd
import json
from PhishingDomainDetection.entity import EvaluationConfig
import joblib
from PhishingDomainDetection.utils import save_reports
import os


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def load_test_data(self):
        datapath = self.config.load_test_data
        self.df = pd.read_csv(datapath)
    
    def load_model(self):
        model_path = self.config.load_model_path
        self.model = joblib.load(model_path)

    def evaluation(self):
        x_test = self.df.drop("phishing", axis=1)
        self.y_test = self.df['phishing']

        self.y_pred = self.model.predict(x_test)

    
    def save_score(self):
        test_accuracy = accuracy_score(self.y_test, self.y_pred)
        f1_model_score = f1_score(self.y_test, self.y_pred)
        scores = {
            'test_aaccuracy': test_accuracy,
            'f1_score': f1_model_score
        }
        
        evaluation_root_dir = self.config.root_dir
        score_file_dir = self.config.local_file
        raw_score_file_path = os.path.join(evaluation_root_dir, score_file_dir)

        save_reports(scores, raw_score_file_path)