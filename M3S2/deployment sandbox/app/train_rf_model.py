import numpy as np
import pandas as pd

# Read the Data

data = pd.read_csv('./data/df_scaled.csv')

# Text Preprocessing

import re # regex library
from sklearn.preprocessing import OrdinalEncoder

# Train, Test Split

from sklearn.model_selection import train_test_split

X = np.array(data['Age_adj']).reshape(-1, 1)
         #  'gender', 'hypertension', 'heart_disease', 'ever_married',
         # 'work_type', 'Residence_type', 'smoking_status',  
         #  'AgeGroups', 'avg_glucose_level_n', 'bmi_n']]
y = data['stroke']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a Random forest Pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


rf_pipeline = Pipeline([#('scale', StandardScaler()),
                         ('rf', RandomForestClassifier())])

rf_pipeline.fit(X_train, y_train)

# Testing the Pipeline

y_pred = rf_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print('Accuracy: {} %'.format(100 * accuracy_score(y_test, y_pred)))

# Saving the Pipeline

from joblib import dump
dump(rf_pipeline, 'rf_classifier.joblib')