import numpy as np
import pandas as pd
import joblib
import re
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from fastapi import FastAPI

app = FastAPI()

model = joblib.load('gbm_classifier.joblib')

def preprocessor(age: int):
    age = int(age)
    
    return age

def classify_patient(model, age):

    age = np.array(preprocessor(age)).reshape(1, -1)
    label = model.predict(age)[0]
    stroke_prob = model.predict_proba(age)
    
    return {'label': label.item(), 'stroke_probability': stroke_prob[0][1]}

@app.get('/')
def get_root():

    return {'message': 'Welcome to the stroke detection API'}

@app.get('/stroke_detection_query/')
async def detect_stroke_query(age: int):
    return classify_patient(model, age)

@app.get('/stroke_detection_path/{age}')
async def detect_stroke_path(age: int):
    return classify_patient(model, age)