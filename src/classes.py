# Standard Imports
import numpy as np
import pandas as pd

# Model Evaluation
from sklearn.model_selection import cross_val_score, KFold

class ModelHistory:
    
    def __init__(self, scorer, random_state = 45):
        self.scorer = scorer
        self.history = pd.DataFrame(columns = ['Name', 'Accuracy', 'Notes'])
    
    def report(self, model, X, y, name, notes='', cv=5):
        kf = KFold(n_splits = cv, random_state = 45, shuffle = True)
        scores = cross_val_score(model, X, y, scoring = self.scorer, cv = kf)
        self.log_report(name, scores.mean(), notes)
        print('Average Score:', scores.mean())
        return scores
    
    def log_report(self, name, av_score, notes):
        frame = pd.DataFrame([[name, av_score, notes]], columns = ['Name', 'Accuracy', 'Notes'])
        self.history = self.history.append(frame)
        self.history = self.history.reset_index(drop = True)
        self.history = self.history.sort_values('Accuracy', ascending = False)
    
    def print_accuracy(self, name, accuracy):
        print('{} has an average error of ${:.2f}'.format(name, accuracy))
