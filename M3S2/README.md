# Stroke Prediction

## Introduction

In this project I will train and deploy a machine learning model on the Stroke Prediction Dataset. We will imagine that I am a data analyst working for The Johns Hopkins Hospital. And we need to create a machine learning model, which could predict if the patient is likely to get a stroke - being able to determine which patients have high stroke risk will allow the doctors to advise them and their families on how to act in case of an emergency.

The aim of this project is to run the EDA, applying statistical inference procedures, try using various types of machine learning models and after the selecting the best performin model deploying it.

## EDA questions

For the EDA we will raise these questions and Assumptions:
- How many patients had a stroke?
- How patients distributes per gender and if they had a stroke? 
- Is there any gender effect on the possibility to have a stroke?
- Does age has impact on strokes? And how is this parameter distributed?
- Does body mass index and glucose levels in a person, propel a heart stroke?
- Assumption: Smoking can induce Stroke, is it true?
- Assumption: Heart with a Heart Disease is prone to Stroke?
- Assumption: Work type might results in more stress and that could lead to Stroke, is it true?

All these questions and assumptions should give insighs on the potential significant features to include in the model.

## Approach
- First, we will run data prepration and overview if data needs data cleaning.
- Then we will run EDA based on raised questions and assumptions.
- We will do feature importance and feature selection for accurate predictions exercise.
- We will try different ML models to choose from the best which predicts most accurately the stoke probability.
- Finally we will deploy the best performing model.


## Datasets columns
- <i>id</i> - Identification number of the individual.
- <i>gender</i> - Gender of the individual.
- <i>hypertension</i> - Health related parameter, does person have hypertension.
- <i>heart_disease</i> - Health related parameter, does person have heart disease.
- <i>ever_married</i> - Personal information, is person married on not?
- <i>work_type</i> - Nature of work place.
- <i>Residence_type</i> - Residence type of the individual.
- <i>avg_glucose_level</i> - Average glucose level in blood for the individual.
- <i>bmi</i> - Body mass index of the individual.
- <i>smoking_status</i> - Habitual information. Current smoking status of individual.
- <i>stroke</i> - Our taget, is person suffered heart attack?

## Conclusions
### EDA
- The dataset is highly unballanced, there is minority of patients who had store (4.87%) and if we want to predict if patient might have a stroke there is too small sample to learn from. We will need to use sampling techniques to balance the dataset.
- Genger might not make the impact regarding stroke possibilities. Based on this dataset there is 5.11% of males and 4.71% of females who had a stroke. The hypothesis on the the proportions difference was rejected which means, in population gender might be insignificant factor for the stroke probability.
- Age might increase the risk to have a stroke. The older patient is, the higher proportion of patients had a stroke. Dataset patients distribution and hypotjesis testing on the proportion difference have validated that age might have the impactto stoke probability.
- Patients who had a stroke avg. glocose level was significantly higher than patients without a stroke. High avg. glocose lebel might indicate the risk of having stroke. Avg. glocose level of patients who had stroke might vary between (124.81595184381645, 140.27352606783) with 95% confidence.
- There was aslo higher proportion of the patients who had a stroke with these conditions: had hypertension, heart deseases, was self-employed or was formerly smokers.

### Feature engineering
- The PCA analysis showed taht using 8 principal components instead of 9-11 is fine because they can capture 90%+ of the variance.
- PCA1 is made from 28% of age (adjusted value), 20% of ever married, and 13% of Age group. PCA3 is most made from gender (41%). PCA4 is primarily dominated by residential type.

### Modeling
- The best performed model was GradientBoost Classifier after hyperparameter tunning. Accuracy increased from 92.95% to 97.05%.
- The second best candidate model to predict patient probability to have a stroke is Random forest with default parameters configuration. Accuracy = 96.93%.
- We saw that age, smoking status, avg. glocose level and BMI are the most important features when it comes to predicting stroke-prone individuals, based on the current dataset.


## Useful links
- https://towardsdatascience.com/principal-component-analysis-pca-explained-visually-with-zero-math-1cbf392b9e7d
- https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/
- https://www.kaggle.com/code/dansbecker/shap-values
- https://www.kaggle.com/code/joshuaswords/predicting-a-stroke-shap-lime-explainer-eli5
- https://www.kaggle.com/code/thomaskonstantin/analyzing-and-modeling-stroke-data

