import numpy as np
import pandas as pd
import joblib
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.under_sampling import RandomUnderSampler

from fastapi import FastAPI, File, UploadFile, Request

app = FastAPI()

model = joblib.load('rf_classifier.joblib') 
scaler = joblib.load('standard_scaler.pkl') 
    
@app.get('/')
def get_root():

    return {'message': 'Welcome to the loan grade classiffier API'}


@app.post("/predict/")
async def predict(request: Request, file: UploadFile = File()):
    body = await file.read()
    json_data = body.decode('utf-8')
    input_data = pd.read_json(json_data)
    data = pd.DataFrame.from_dict(input_data)
    print(data)
    
    #data_stg = scaler.fit_transform(data)
    #features = pd.DataFrame(data_stg, columns=list(data.columns))
    features = data
    print(features)
    
    label = model.predict(features)[0]
    print(label)
    label_index = int(label.item())
    
    grade_prob = model.predict_proba(features)
    print(grade_prob)
    
    ordinal_mapping_grade = {'0.0': 'A', '1.0': 'B', '2.0': 'C', '3.0': 'D', '4.0': 'E.0', '5.0': 'F', '6.0': 'G'}
    
    return {"message": "Prediction done successfully", 'label': ordinal_mapping_grade[str(label.item())], 'grade_probability': grade_prob[0][label_index]} 
