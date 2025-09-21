# Red Wine Quality Analysis And Statistical Modeling

## Introduction & Approach

We will run the analysis of the red variants of the Portuguese "Vinho Verde" wine and apply some statistical modeling. We will use data source from Kaggle (https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

First, we will do EDA for the dataset overview and will answer these questions: 
- How many wine records are in the dataset?
- What is the unique quality ratings?
- What is avg., median and percentiles of wine quality?
- How wide distributes per quality ratings?
- How many good and bad ratings having wines are?
- What other wine attributes statistics are?
- Red wine attributes distributions?
- Is there any outliers? Do we need to clean and preparte data?

Second, we will analyze if any linear relationships exists between wine attributes and prepare for the linear regresion modeling to predict one of the wine attributes:
- Does wine attributes correlates with quality rating and with each other?
- We will check if standartisation or normalisation of data is needed.

In statistical modeling part we will want to check 2 cases:
- What features impacts and describes wine alcohol level?
- What linear regresion model best describes wine alcohol level?
- We will try to prepare model which predicts the good quality wine


## Results summary
- There is 1599 red wine records in dataset.
- Red wine can get quality rating from 0 to 10. However, onyl 
- Avg. red wine rating is 5.6, median 6.
- The majority of wines gets 5 (43%) and 6 (40%) quality ratings. Very few gets 7+ quality rating (13%)
- Only 13.6% of wines in datset has good wine quality status.
- Other wine attributes varies and they seem has different scale of values.

- Alcohol best describes model with only highest correlation having features (density, quality) and without constant value. Model quality is very good, R^2 = 0.984, which shows that independend variables describes 98.4% of dependand variable variability. If density increase by 1% point, the alcohol level might decrease by -0.2730 points. The higher wine quality rating, the probably higher alcohol level wine will be.

- Wine quality prediction model with all features is qualitative. ACC = 88.4%, F1 = 93.6% quality metrics. This means, that model 88.4% of times predicts wine quality as god correctly.
- Reducing features amount does not negatively effected the model and its quality. The model quality remained good. (ACC = 88.1%, F1 = 93.4%) This means, that model 88.1% of times predicts wine quality as god.

Data Studio report: https://lookerstudio.google.com/reporting/2dfc1914-6c1b-4c6b-a1a3-9acef39dff12
