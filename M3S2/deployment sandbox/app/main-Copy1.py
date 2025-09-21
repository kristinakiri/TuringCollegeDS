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
# model = joblib.load('rf_classifier.joblib')

def preprocessor(age: int):
                #  gender: str, hypertension: int, heart_disease: int,
                # ever_married: str, work_type: str, Residence_type: srt,
                # smoking_status: str, avg_glucose_level: float, bmi: float):
    age = int(age)
     
            
    # data_in['Age_adj'] = np.where(data_in.age < 2, 2, data_in.age)
    # data_in['AgeGroups'] = np.where(data_in.age >= 65, 1, 0)
    
#     ordinal_encoder = OrdinalEncoder()
#     s = (data_in.dtypes == 'object')
#     object_cols = list(s[s].index)
#     data_in[object_cols] = ordinal_encoder.fit_transform(data_in[object_cols])
    
#     data_in['avg_glucose_level_n'] = data_in.avg_glucose_level/data_in.avg_glucose_level.max()
#     data_in['bmi_n'] = data_in.bmi/data_in.bmi.max()
    
    return age

def classify_patient(model, age):

    age = np.array(preprocessor(age)).reshape(1, -1)
    label = model.predict(age)[0] #model.predict([age])[0]
    stroke_prob = model.predict_proba(age) #model.predict_proba([age])


    #return {'label': label, 'spam_probability': spam_prob[0][1]}

    # return {'label': label, 'stroke_probability': age} 
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