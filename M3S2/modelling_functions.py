import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objects as go
import math

import scipy.stats.distributions as dist
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

from sklearn.preprocessing import OrdinalEncoder
from sklearn import preprocessing

from sklearn.preprocessing import StandardScaler

# balancing dataset
from imblearn.over_sampling import SMOTE

from sklearn import model_selection
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold, GridSearchCV, StratifiedKFold

from sklearn import metrics
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.metrics import precision_recall_curve

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingClassifier
#from xgboost import XGBRegressor
import xgboost as xgb

from sklearn.pipeline import Pipeline

from scipy.stats import reciprocal, uniform

# Tree Visualisation
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz

from IPython.display import clear_output
import warnings
warnings.filterwarnings('ignore')


def fit_model(model_name,classifier,x_train,y_train,x_test,y_test):
    """Fit model"""
    classifier.fit(x_train,y_train)
    prediction = classifier.predict(x_test)
    # clear_output()
    
    print("ROC_AUC Score : ",'{0:.2%}'.format(roc_auc_score(y_test,prediction)))
    fpr, tpr, thresholds = metrics.roc_curve(y_test, prediction)
    roc_auc = metrics.auc(fpr, tpr)
    display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
                                       estimator_name='example estimator')
    display.plot()
    plt.show()  
    
    # Create the confusion matrix
    cm = confusion_matrix(y_test, prediction)
    ConfusionMatrixDisplay(confusion_matrix=cm).plot()
    
    # Classification Report
    #print(classification_report(y_test,prediction))
    
    model_eval = {'model_name': model_name,
                  'acc': accuracy_score(prediction, y_test)*100,
                  'precision': precision_score(y_test, prediction, average='macro')*100,
                  'recall': recall_score(y_test, prediction, average='macro')*100,
                  'f1': f1_score(y_test, prediction, average='macro')*100
                 }
    
    return  model_eval

    
def kfold_cross_validation(model_name,classifier,X):    
    # Cross validation using KFold method
    folds = KFold(n_splits=5)
    folds.get_n_splits(X)
    fold = 0
    acc_f = []
    acc_cv = []
    for train_index, test_index in folds.split(X):
        X_train_cv, X_test_cv, y_train_cv, y_test_cv = X.iloc[train_index], X.iloc[test_index], y.iloc[train_index], y.iloc[test_index]

        model = classifier
        model.fit(X_train_cv, y_train_cv)
        y_pred_cv = model.predict(X_test_cv)
        fold = fold +1
        # clear_output()
        acc_ = accuracy_score(y_pred_cv, y_test_cv)
        acc_cv.append(acc_)
        acc_f_ = {f"acc_in_fold_{fold}": acc_ }
        acc_f.append(acc_f_)

    
    print(*acc_f, sep = "\n")
    print("Cross Validation Score : ",'{0:.2%}'.format(sum(acc_cv) / len(acc_cv) ))