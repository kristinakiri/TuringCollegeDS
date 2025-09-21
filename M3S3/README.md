# LendingClub loans data: analysis and modelling

## Introduction

The lending industry is playing important role in the global economy for the financial services provision, that involves providing loans or credit to individuals, businesses, or governments. Lenders, which can include banks, credit unions, online lenders, and other financial institutions, offer various types of loans such as mortgages, personal loans, business loans, and credit cards.

The lending industry plays a crucial role in providing individuals and businesses with access to capital. Lending is essential for economic growth as it facilitates investment and consumption. It is importnat for the homeownership, businesses development and more.

Wide range of data is generated in such services providing companies. Data analysis is crucial in the lending industry for several reasons, as it helps financial institutions make informed decisions, manage risks, and streamline their processes, provide their services.

There are many use cases in lending sector for data analysis and data science application:
- Risk Assessment - assess the creditworthiness of borrowers
- Credit Scoring - develop credit scoring models to help lenders make quick and consistent decisions regarding loan approvals or rejections
- Portfolio Management - can assess the performance of different loan products, identify trends, and make data-driven decisions to enhance overall portfolio health
- Etc.

In this project we will simulate LendingClub company and try to automate their lending decisions. We will work with the LendingClub's loan data available publically: https://storage.googleapis.com/335-lending-club/lending-club.zip


## Goals

1. To create a machine learning model to classify loans into accepted/rejected.
2. To predict the grade for the loan. 
3. To predict the interest rate.

## Approach
1. Run EDA to explore the dataset and find the insights
2. Implement features engineering
3. Built and develop machine learning models
4. Deploy best performing model to cloud

## Results summary
### EDA
- The Lending club dataset contains huge amount of records collected over the 2007-2018 years (2M+). 2015-2018 was the peak year, where was issued more than 400K loans per year.
- The portfolio consisted from 3 main loans types: 
    - Mortgage type loans (~ half of the portfolio),  
    - Rent type loands (~38-40% from whole portfolio per year) 
    - Own type loands (~10-12% from whole portfolio per year) 
    - and other.
- Most of the loans issued were in the range of 8000 to 40,000 USD (25th & 75th percentiles)
- It was noticed, that Rent type loans tend to get more often bad ratings and the proportional difference were significant based on hypothesis testing statistics. As well as avg. interest rates, there was a significant difference between Mortgage and Rent type loans avg. interest rates.
- Based on Fico ratings and score meaning it looks like that LendingClub has half of their loans at least "Good" Fico score rating (median is 690), 25% of loans might have "Very good" FICO score (75th percentile is 715). And does not have the worst rating loans called "Poor". The lowest Fico score is 610 and 25th percentile is 675, which falls under "Fair" rating group.

### Loans clasification: accepted/rejected
- We assumed that Loan accepted will be Fully paid and Current loan status having loans. And Loan rejected loans having statuses Charged-off, Default.
- For loans clasification it was selected time period of 2015-2017 of loans issued.
- There was only 14% of rejected loans, which showed that we have highly imbalanced dataset.
- The sample of the loans was splitted in to train and test samples. Data cleaning, normalisation, standartisation, categorical values preparation was made separately for train and test samples.
- We have applied undersampling technique to balance dataset target values.
- The best performed model was Random forest with scalled data and after hyperparameter tunning using datasets after undersampling. F1 score increased was 65.57%.
- The second best candidate model to predict loand rejection probability is Logistic Regresion with default parameters and after hyperparameter tunning configuration. F1 = 65.51%.
- Very similar results provided and Gradient Boosting Classifier (F1 = 65.5%)
- The least performance was from Decision Tree and KNeighbors Classifiers.

### Loans grade prediction
- We have used only 2016 year loans records to predict the grades.
- We saw, that better results for random forest provides oversampled dataset with scalled features data. However, it takes too long to train the model and predict. We have tried models with undersampled train and test samples, too.
- The best performed model was Random forest with scalled data and after dataset oversampling. F1 score was 89.1%.
- The second best candidate model was same Random forestwith scalled data and after dataset oversampling but with applied hyperparameters tunning (HT). F1 = 89%.
- Decission tree HT, Logistic regression and Gradient Boosting Callasifier also gave good results f1 was 87+%.

### Loans interest rates prediction
- We used simple linear regresion and machine learning models to discover for the best performing model and resuls.
- To improve features, we incorporated USA federal interest rates on monthly basis the loan was issued. Loans interest rates consists of variuos parts, one of the is federal interest rates, this should add additional information of the market situation.
- Based on the models quality metrics like MAE, MSE and RMSE the best performing model was Random foreset and Decision tree.
- The second best model was Gradient Boosting.
- Even clasical linear regresion models had high R^2 results, but based on the error rates ML models performed better.


## Additional information
### Domain definitions and features meaning

- Credit risk - is the probability of a financial loss resulting from a borrower's failure to repay a loan. Essentially, credit risk refers to the risk that a lender may not receive the owed principal and interest, which results in an interruption of cash flows and increased costs for collection.
- Debt-to-income ratio (DTI) - is all your monthly debt payments divided by your gross monthly income. This number is one way lenders measure your ability to manage the monthly payments to repay the money you plan to borrow.

- `loan_amnt` - The listed amount of the loan applied by the borrower.
- `term` - The number of payments on the loan, where values are in months and can be either 36 or 60.
- `int_rate` - The interest rate on the loan
- `sub_grade` - Assigned loan subgrade score based on borrower's credit history
- `emp_length` - Borrow's employment length in years.
- `home_ownership` - The homeownership status provided by the borrower (e.g., rent, own, mortgage, etc.)
- `annual_inc` - The self-reported annual income provided by the borrower
- `addr_state` - The state provided by the borrower in the loan application
- `dti` - A ratio calculated using the borrower's total monthly debt payments on the total debt obligations, excluding mortgage, divided by the borrower's monthly income.
- `mths_since_recent_inq` - Months since most recent inquiry
- `revol_util` - Revolving line utilization rate, or the amount of credit the borrower uses relative to all available revolving credit.
- `bc_open_to_buy` - Total open to buy on revolving bankcards
- `bc_util` - Ratio of total current balance to high credit/credit limit for all bankcard accounts
- `num_op_rev_tl` - Number of open revolving accounts
- `loan_status`  - Current loan status (e.g., fully paid or charged off). This is the label we are going to predict with the model.
- `instalment` - an installment loan is a type of agreement or contract involving a loan that is repaid over time with a set number of scheduled payments;[1] normally at least two payments are made towards the loan. The term of loan may be as little as a few months and as long as 30 years. A mortgage loan, for example, is a type of installment loan.
- `fico score range` - A credit score is a number that is used to predict how likely you are to pay back a loan on time. The overall FICO score range is between 300 and 850. In general, scores in the 670 to 739 range indicate a “good” credit history and most lenders will consider this score favorable. In contrast, borrowers in the 580 to 669 range may find it difficult to get financing at attractive rates.
- `inq_last_6mths` - The number of inquiries in past 6 months (excluding auto and mortgage inquiries).
- `total_acc` - The total Number of credit lines currently.
- `delinq.2yrs` - The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
- `earliest_cr_line` - The date the borrower's earliest reported credit line was opened.
- `inquiries during last 6 months` - Inquiries happen when a financial institution checks your credit to make a lending decision.
- `pub.rec` - The borrower’s number of derogatory public records (bankruptcy filings, tax liens, or judgments).

Consider only business critical features:
`[['loan_amnt', 'term','int_rate', 'sub_grade', 'emp_length','grade', 'annual_inc', 'loan_status', 'dti',
'mths_since_recent_inq', 'revol_util', 'bc_open_to_buy', 'bc_util', 'num_op_rev_tl']]`
    

## Sources
1. https://www.investopedia.com/terms/c/creditrisk.asp
2. https://www.investopedia.com/terms/c/credit_scoring.asp
3. https://www.investopedia.com/terms/f/ficoscore.asp
4. https://medium.com/analytics-vidhya/testing-a-difference-in-population-proportions-in-python-89d57a06254
    

    
