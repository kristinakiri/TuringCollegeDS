# Inferential Statistical Analysis of the iTunes Podcast Reviews

## Introduction and goal

This analysis purposes are to practice performing EDA, applying statistical inference procedures and creating dashboards with Google Data Studio. 

First of all, we will overview iTune Podcats data and run a data preparation, standartization, normalization if needed.
Then, we will prepare aggregated data set and defined metrics, dimensions for the Podcasts overview report in Data Studio. (`iter1` python file).

By this overview report we will want to answer the following questions:
- How many unique podcasts are in this dataset?
- What unique categories podcasts have?
- How podcasts distributes per categories?
- How many reviews were collected?
- Which categories podcasts got the most reviews?
- What is an average review number per podcasts?
- What is an average rating per podcast?
- What is the average rating per podcasts categories?

Besides we want to check if there is any linear relationship between number of reviews and ratings. And see how many reviews iTunes collects on daily basis for their Podcasts.

Later, we will move to inferential statistical analysis for deeper data analysis and hypothesis testin (`iter2` python file)

Based on the dataset we will want to validate few statements:
1. Most popular category (comedy) podcasts gets best reviews.
2. Bad reviews tend to grow more over crisis years than in economical, social growth time.
3. Reviews length differs significantly per negative and positive ratings.

For these statements we will prepare sample metrics. Form hypothesis. Test them and estimate confidence intervals for the metrics. 
After received estimates and results we will make conclusions about these statements.

## Analysis findings

### General overview

In this data set we had 110 024 unique podcasts, which distributes into 3621 unique categories combinations. In iTunes Podcats you can find 116 unique categories podcasts.

Most podcasts are under culture (6.8%), society (6.8%), education (4.6%), business (4.6%), comedy (4.6%), spirituality (4.3%) and religion (4.3%) categories. 

But most reviews got comedy (99.8K), crime-true (77.2K), culture-society (68.4K) categories Podcasts.

In general more than 2M reviews were collected over 2005-2023, on avg. 18.6K reviews were left per podcasts and on avg. podcast have 4.8 rating.


### Statistical inferential analysis findings
- Comedy podcast might have possibility to get very good rating. We estimated, with 95% confidence, that the population proportion of comedy podcasts with 5 star ratings might be somewhere between 87.7% and 88.1%.
- Proportion of Bad reviews compared with growth years 2011-2019 and crisis years 2020 - 2023 increased. As well as avg. rating also decreased per all categories on crisis years.
- After testing hypothesis whether negative ratings proportions differ and avg. rating differ between growth and crisis years, we rejected NULL hypothesis and concluded that difference is significant. Thus, we might state that bad reviews tend to grow more over crisis years than in economical, social growth time.
- Users might leave longer negative reviews. We have made such conclusion after testing hypothesis that reviews length differs significantly per neagtive and positive ratings.

## Links
- Report link: https://lookerstudio.google.com/u/0/reporting/5089298a-93a2-4247-b2bf-11c51ae96c97/page/tEnnC

- Bigquery project and datasets: https://console.cloud.google.com/bigquery?project=tcm2s2podcats&supportedpurview=project&ws=!1m5!1m4!4m3!1stcm2s2podcats!2situnepodcats!3spodcasts

- Podcast Reviews Dataset: https://www.kaggle.com/datasets/thoughtvector/podcastreviews/versions/28