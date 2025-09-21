# Football matches

## Context
Football is one of the most popular team sports in the world. Globally, association football is played by over 250 million players in over 200 nations. 

Many competitions are happening over the year and the major global events attracts millions spectators. The biggest and the most famous international tournament of Football is The World Cup which is organized by FIFA. This competition takes place once in every four years. There are approximately 190 to 200 national teams competing to qualify in this tournament. There are other huge tournamenets like: 
- European Championship (UEFA), 
- The Copa America (CONMEBOL)
- African Cup of Nations (CAF)
- The Asian Cup (AFC)
- The CONCACAF Gold Cup
- The OFC Nations Cup (OFC)
There are many champions league tournaments conducted between the Football clubs, and so on.

It is hard to deny, that football is very impartant and popular sport.

Football attracts not only spectors but also the analytics who analyses teams, players performance and helps to improve the for athletes and teams. It is also very popular object for betting and predicting how the tournaments will end up.  



## Analysis goal 

The analysis goal is to analize the dataset and find factors impacting scorring results individualy per athlete.
We will try to find the model which best describes player rating and to predict it.

Later we will try to find out which league is most competitive and most predictable and which are the least.
And how we can predict the match outcome - if team will win.

Analysis questions:
- Which leagues are in which countries?
- How many teams are present in each league? 
- Which league has the most team?
- Which leagues score the most/fewest goals?
- Which players is the top players?
- Who are the top scorers in each team and league?
- Is there such a thing as home advantage?
- Can we predict player rating - potential? What key factors defines that?

## Conclusion

<b>Players</b>
- In this dataset there is 10.410 unique players information present. Over the years # of players varied, and on 2016 there was 5.586 player records found.
- There is various age players in the dataset when thei were first time registered in it. Starting from 8 year old to 38. The majority of players registered in this dataset is between 15-19 and 20-24 years old (33.7% and 29.1%). 
- Significant majority of the players remained in football and this dataset register over the years (from 2007 to 2016).
- Avg. player height is 181.9 and avg. weigth is 168.8.
- Google studio report about playes: https://lookerstudio.google.com/reporting/3707713e-490c-4d8f-83ad-b536227fe469
- Top 5 playeres having the highest ratings: 
    1. Lionel Messi 94.0
    2. Cristiano Ronaldo 93.0
    3. Luis Suarez 90.0
    4. Manuel Neuer 90.0
    5. Neymar 90.0

<b>Leagues and teams</b>
- There is 11 leagues in 11 countries.
- Most of the countries and leagues has similar high number of teams. Around 30 teams. Most teams having leagues are: France Ligue 1 (35), England Premier League (34), Spain LIGA BBVA (33). While least teams having leagues are: Switzerland Super League (15), Scotland Premier League (17), Poland Ekstraklasa (22).
- The most goals in total scores leagues: Spain LIGA BBVA, England Premier League, Italy Serie A. While the fewest goals scores leagues: Switzerland Super League, Poland Ekstraklasa, Scotland Premier League.
- Based on macthes mean, best scores: Netherlands Eredivisie (3.1), Switzerland Super League (2.9), Germany 1. Bundesliga (2.9). Lowest matches goals mean is on: Poland Ekstraklasa (2.4), France Ligue 1 (2.4), Portugal Liga ZON Sagres (2.5).

<b>Home advantage</b>
If home advantage playing the match and perform better appears, it was analysed base on 3 attributes: shoton, cross and goals.
- Based on shoton distribution it seems that home teams tend to make more shots on goal than away teams.
H0: Shoton number difference means between Home and Away league teams is equal. (μ1=μ2)
After testing hypothesis, we rejected H0 and conclude that avg. shoton number difference means between home and away teams is significant different from 0. We can interpret that avg. shoton number between home and away teams differs. And avg. shoton number difference between home and away teams might vary from 0 to 5.9 shots.
- H0: Cross difference means between Home and Away league teams is equal. (μ1=μ2). Based on distribution - home teams tend to make more passes, averaging around 20.
We reject H0 hyppthesis, and conclude that avg. cross difference means between home and away teams is significant different from 0. We can interpret that avg. cross between home and away teams differs. Avg. cross value difference between home and away teams might vary from 0 to 18.6 shots.
- Based on goal number we saw that more home team matches are with 2 or more goals than away teams. Which allows make assumption that home teams might score more goals than away teams.

<b>Players ratings prediction</b>
- Players overall rating has strong correlation with the potential (0.84), then with reaction (0.79). Moderate correlation is with vision (0.49).
- Linear regressiom model with independant variable `potential` gives r-squared of 70.9%  model and reveals that 70.9% of the variability observed in the target variable is explained by the regression model. If the potential increases by 1 point overall rating might increase by 0.876 points. However, constant estimate is higher (5.398), which shows that there is more unobserved factors impacting overvall rating value.
- Similar is with second model where reactions is independant variable. The model quality is moderate and 62% of variability observed in the target variable is explained by the regression model. If the reactions increases by 1 point overall rating might increase by 0.599 points.
- Other models with other attributes are poor and does not describe well overall rating.
- To predict what overall rating player might have the Liner regresion model with all numeric features from dataset gives good quality results (R^2 is hight (0.88). RMSE is also low (2.3). Which shows that model is quite good.)
- Reducing number of features in the model and leaving these attributes with high or moderate correlations also gives good model with R^2=0.859 and RMSE=2.6

<b>League predictability</b>
- We can see that he Spanish league has been the least competitive league out of the all leagues in the dataset.
- Contraro to, the French league is the most competitive one. 
- The English league has changed its position in time, raising its rank to the 2nd most competitive league in 2015/2016. 
- Italy over the years remained quite stable and in second most competitice league position. 
- Germany and Portugal was quite decreasing over the years.

<b>Matches outcome prediction</b>
- To predict if home team will win Logistic Regresiom model with teams performance attributes as model features performs quite good. The model quality is ACC = 75.3%, F1 = 74.9%. This means, that model 75.3% of times predicts that home team would win.
- Added teams players ratings attributes does not helped to improve the model, accurasy decreased slightly (ACC=72%, F1 = 71.3%)

# Links
- https://en.wikipedia.org/wiki/Football
- https://www.youtube.com/watch?v=FZ4i3KX2CW4
- https://www.fifplay.com/encyclopedia/work-rate/#:~:text=The%20Work%20Rate%20is%20defined,they%20are%20out%20of%20position.
- https://www.topendsports.com/sport/soccer/terms.htm
- https://en.wikipedia.org/wiki/Continental_football_championships
- https://www.tutorialspoint.com/football/football_tournaments.htm
- https://en.wikipedia.org/wiki/Entropy_(information_theory)
- https://labtwentyone.tumblr.com/post/147894684062/why-did-we-stop-loving-football
- https://www.kaggle.com/code/yonilev/the-most-predictable-league/notebook

