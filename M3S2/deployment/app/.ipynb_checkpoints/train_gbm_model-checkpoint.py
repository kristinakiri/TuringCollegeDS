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
y = data['stroke']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a GradientBoostClassifier Pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier


gbm_pipeline = Pipeline([('gbm', GradientBoostingClassifier(learning_rate=0.1,max_depth= 9,n_estimators= 500))])

gbm_pipeline.fit(X_train, y_train)

# Testing the Pipeline

y_pred = gbm_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print('Accuracy: {} %'.format(100 * accuracy_score(y_test, y_pred)))

# Saving the Pipeline

from joblib import dump
dump(gbm_pipeline, 'gbm_classifier.joblib')