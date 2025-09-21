# Travel Insurance Data Analysis And Prediction

## Introduction
A Tour & Travels Company Is Offering Travel Insurance Package To Their Customers. As all companies seeks to increase sales of their servises, they want to know their customer  and if they will be interested to buy the insurance. 

The company has collected many data about their previous customers. Its in in their database history. There are almost 2000 previous customers records. Based on the data they want to build an model, which could predict if the customer will be interested to buy the travel insurance package and which features impacts the purchase.

## Analysis goal and approach
For this goal we will run the EAD and apply statistical inference to get better Travel insurance company customers. We will compare the customer groups and if there is significant differences betveen them. Is there any significant differences in proportions - conversions to purchase travel insurance between:
- Employment type
- Age groups - if older customers tend to purchase travel insurance more often.
- Annual income groups - if more annual income getting customers more purchase insurance.
- Travel habbits - frequet travelers more frequent purchase the insurance.

Later we will try to built the model to predict if customer is willing to buy the insurance.



## Conclusions

- The company customer base consists of 1987 customer records. The company customers are quite young between 25 - 35 years.
- Customers annual incomes varies - median yearly income is 900.000 indian rupees. 25% of least yearly incomes getting customers earn between 300.000 - 600.000 yearly (min, 25th percentile). And 25% the most yearly incomes getting customers earn between 1.250.000 - 1.800.000 yearly (75th percentile, max).
- The companies customer conversion to travel insurance purchase is moderate. A bit more than 1/3 of customers bought travel insurance (35.7%).
- There is bigger proportion of customers who purchases travel insurance if they are working in private sector or self employed, than working in goverment sector (40.23% vs. 24.56%).
- Even 28 old customers are the biggest group in the company client base, but they are among least purchasing the travel insurance. Only 20.75% of this age customers purchased it. But the volume is still hight. The highest conversion to purchase the insurance is 33+ year olds and 25-26 years old (~50% purchases it). Somehow the least conversions to purchase is amont 27-29 years old.
- If the customer is 30+ years old it might be more often that he/she will purcase traveling insurance.
- The higher annual incomes are, the higher conversion to insurance purchae might be.
- Traveling frequency might have impact to purchase insurance, too. Freuquent flyer customers proportio who bought insurance is higher and significant.

- The best model to predict if customer purchase the travel insurance is Decision Tree Classifier model after hyperparameters tunning (max_depth=6, max_features=4). This model accuracy is 83.081761%.
- GradientBoostingClassifier, Random Forest Classifier, Neighbors Classifier clasifies customers whether they will purchase the travel insurance gives also good results.
- The most impact to the model has these attributes: Annual income, Family members and customer age.

## Links
1. Data sourse: https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data
