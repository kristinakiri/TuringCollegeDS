# Analysis of the Mental Health in the Tech Industry

## Introduction

This project purpose is to analyse the Mental Health in the Tech Industry Dataset. To explore and find how often mental health disorders are met among the  tech workplace? Does gender or age, company size has any impact for mental health vulnarability? Does people became more open about mental health issues topics overall?

For this analysis we will use survey dataset from: https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry

Files format is SQLite and the file contains 3 tables:
- Survey -  all surveys used.
- Question - all questions used for each survey.
- Answer - every answer(answertext) for a given user (userid) and the survey year (surveyid).

## Approach

- First, we will load the data files using SQLlite api `sqlite3` module.
- We will perform data overview and data cleaning, standartization and normalization.
- Later, we will select the most interesting questions from survey and design the analysis questions and hypotesis to run the EDA.
- We will perform EDA
- And finally collect the most interesting findings.

## EDA questions & hypothesis

At the begining we want to understand when and how many respondents where involved to the surveys. And understant the sample composition per gender, age and geography. Thus, these questions will allow to draw general picture about the conducted surveyes:
1. On which years surveys were conducted?
2. What was the surveys respondents sample size?
3. What are the surveys gender composition?
4. What are the surveys age composition?
5. What is the geographical respondents distribution?

Then, we want to understand the general situation about mental health among Tech companies:
1. How often mental heath disorder (MHD) is met among the tech workplace?
2. What conditions of MHD are most often met?
3. Are there any differences per gender of having MHD?
4. Are there certain age groups where MHD are met more often?

Finally, we want to form and check few hypothesis of the mental health disorders among employees:
1. H0: The more employees organization has the more MHD cases could be meet.
2. H0: People with MHD working at companies, which have benefits for mental health support, experience less work interfence and are more productive.
3. H0: Over time confidence to share about MHD is changing, people became more open.

## Conclusions

Overall, from the analysis we can see that many people suffers and experience one or another conditions of mental health disorders. In tech industry companies, 60% people identifies they have MHD. Most often it is related to Mood disorders (Depresion, Bipolar disorder, etc) (52.8%). 
    
Even all genders might experience MHD, but a bit more females and other gender said they has/had diagnozed MHD. More males between 30-40 years old (45.5%) and more younger womens between 20-30 years old (43.8%) and other gender people between 20-40 years old.
    
If the companies supports their employees with mental health benefits it helps them to keep productivity and avoid productivity loss effects.
    
Finally, we can see that mindest about MHD changes over time, people became more open to share about their mental health with their coworkers and supervisors.
    

### Detailed findings

Survey general samples size overview:
- The surveys were taken almost every year from 2014 to 2019, but 2015 was skipped.
- Over the years, some questions remained the same, but there were some which was stopped, changed, or similar new were introduced.
- Number of surveys participants differs per survey year. Sample size was decreasing. 
- There are more males participating in the surveyes than females or other gender participants. But over time surveys gender proportions changed: proportion of males slightly decreased and females increased. While in last 3 years more people specified other genders than male and female, too.
- The average age of the participant in the survey was between 32-35 years. Median was 31-34. The one of the youngest participants were around 27-29 years old (25th percentile) and oldest were around 36-41 years old (75th percentile).
- The most participants were from United States and Unted Kingdom.

Mental health situation among Tech companies:
- The surveys showed that quite many people suffers from mental health disorders (MHD). There was more than 60% od respondents who have or had MHD. The percentage remained high over all surveys taken per years.
- 52.8% of respondents mentioned that they have MHD diagnozis of Mood disorders (Depresion, Bipolar disorder, etc). 8.3% said they have Anxiet Disorder (Generalized, Social, Phobia). In third place most often mentioned MHD was Post-traymatic Stress Discorder (8.1%). As well respondents say they struggle from substance use, stress response syndrome, attention deficit, hyperactivity, obsessive-compulsives disorders.
- It looks like that more often MHD had womens and other gender people. In latest surveys more women and other gender people say they have MHD (more than 70%). Then males having MHD proportion is up to 60%.
- There are more mid age males (30-40 years old) and more younger womens (between 20-30 years old) having MHD. 45.5% males and 43.8% females. There was a lot other gender people having MHD between 20-40 years old.
- The percentage of MHD having people from total survey participants looks like increasing by the increasing number of employees per organization on all taken surveys. Except 500-1000 employees companies.
- 34% from total respondents has MHD, works in companies having benefits for mental health and say they work productivity is not effected due to their condition. And 6.5% of respondents having MHD said they productivity is effected and do not get any mental heath benefit from company.
- The analysis shows, that more percentage of people are willing to share about MHD with their colleagues over the time. Similar situation is with sharing with supervisor. Since 2016 up to 2018 percent of respondents saying they are willing to speak about MHD with superviser increased by 10% points (from 58% to 68%). Thus, we might assume, that employeers became more open and startted to trust more with their supervisers to speek about MHD.