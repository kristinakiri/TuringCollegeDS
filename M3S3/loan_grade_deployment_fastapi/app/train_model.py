import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score

import joblib
from joblib import dump
from sklearn.ensemble import RandomForestClassifier


# Read the Data
df_x = pd.read_csv('./data/x_train_ohot_en.csv')
df_y = pd.read_csv('./data/y_train_ohot_en.csv')

# Oversampling
sm = SMOTE()

X_train, y_train = sm.fit_resample(df_x, df_y) 

# Scaling
scaler = MinMaxScaler()

X_train_s = scaler.fit_transform(X_train)
X_train = pd.DataFrame(X_train_s, columns=list(X_train.columns))


# Initialize and train the Random Forest model
rf_pipeline = Pipeline([('classifier', RandomForestClassifier())])

rf_pipeline.fit(X_train, y_train)

# Save the scaler object
joblib.dump(scaler, "standard_scaler.pkl")

# Saving the trained model
dump(rf_pipeline, 'rf_classifier.joblib')

joblib.dump(rf_pipeline, 'trained_model.pkl')