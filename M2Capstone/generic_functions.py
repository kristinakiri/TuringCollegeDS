from termcolor import colored
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring, ElementTree

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, clear_output
from datetime import datetime


def check_duplicates(df):
    """This function checks if dataframe length is same
    after the duplicate rows removal"""
    
    if len(df) == len(df.drop_duplicates()):
        print('Table does not have duplicate rows')
    else:
        print(colored('Table has duplicates rows','red'))
    
def check_missing_values(df):
    """This function checks if dataframe length is same
    after the missing values having rows removal"""
    
    if len(df) == len(df.dropna()):
        print('Table does not have missing values')
    else:
        print(colored('Table has missing values','red'))
        
        
def extract_xml(row,col_name,xml_key,away_home):
    count = 0
    
    element = row[col_name]
    team_id = row[away_home + "_team_api_id"]
    
    if type(element) == int:
        return element
    
    elif element != None:
       # print(row,element)
        tree = ElementTree(fromstring(element))
        root = tree.getroot()
        
        for child in root.iter(xml_key):
            
            if str(team_id) == child.text:
                count +=1
        return count
    else:
        return np.nan
    
    
## Top Players, Teams and leagues ratings:

def end_of_year_player(df_comb_player,year):
    df_comb_player['date'] = pd.to_datetime(df_comb_player['date'])
    df_comb_player = df_comb_player[df_comb_player['date'].dt.year == year]
    df_comb_player = df_comb_player.sort_values('date').groupby('player_api_id').last()    
    df_comb_player.reset_index(level=0, inplace=True)
    return df_comb_player[['player_api_id','player_name', 'date', 'overall_rating', 'potential']]

def end_of_year_team(df_comb_team):
    df_comb_team = df_comb_team.sort_values('date').groupby('team_api_id').last()
    df_comb_team.reset_index(level=0, inplace=True)
    return df_comb_team[['team_api_id','team_long_name','date']]

def team_to_player_home(df_match,year):
    players_list_home = ['date','home_team_api_id','home_player_1', 'home_player_2', 'home_player_3',
   'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7',
   'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']
    df_match = df_match.loc[:,players_list_home]
    df_match['date'] = pd.to_datetime(df_match['date'])
    df_match = df_match[df_match['date'].dt.year == year]
    df_match = df_match.drop(['date'],axis=1)
    df_team_to_player=df_match.melt(['home_team_api_id']).sort_values('home_team_api_id')
    df_team_to_player = df_team_to_player[["home_team_api_id","value"]]
    df_team_to_player.rename( columns={"value":"player_api_id", "home_team_api_id":"team_api_id" },inplace=True)
    df_team_to_player = df_team_to_player.drop_duplicates()
    df_team_to_player = df_team_to_player.dropna()
    return df_team_to_player

def team_to_player_away(df_match,year):
    players_list_away = [ 'date','away_team_api_id','away_player_1', 'away_player_2','away_player_3', 'away_player_4', 'away_player_5', 'away_player_6',
       'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10','away_player_11']
    df_match = df_match.loc[:,players_list_away]
    df_match['date'] = pd.to_datetime(df_match['date'])
    df_match = df_match[df_match['date'].dt.year == year]
    df_match = df_match.drop(['date'],axis=1)
    df_team_to_player=df_match.melt(['away_team_api_id']).sort_values('away_team_api_id')
    df_team_to_player = df_team_to_player[["away_team_api_id","value"]]
    df_team_to_player.rename( columns={"value":"player_api_id", "away_team_api_id":"team_api_id" },inplace=True)
    df_team_to_player = df_team_to_player.drop_duplicates()
    df_team_to_player = df_team_to_player.dropna()
    return df_team_to_player

def team_to_player(df_match,year):    
    df_2 = team_to_player_home(df_match,year)
    df_1 = team_to_player_away(df_match,year)
    df_combined = [df_1,df_2]
    result = pd.concat(df_combined)
    result = result.drop_duplicates()
    return result

def top_N_team(df_comb_team,df_comb_player,df_match,season="2015/2016",n=5):
    year = int(season.split("/")[0])
    df_end_of_year_team = end_of_year_team(df_comb_team)
    df_end_of_year_player = end_of_year_player(df_comb_player,year)
    df_team_to_player = team_to_player(df_match,year)
    df_end_of_year_player = pd.merge(df_end_of_year_player, df_team_to_player, on="player_api_id")
    df_comb_player_team_group= df_end_of_year_player.sort_values('overall_rating').groupby('team_api_id').head(16)
    df_comb_player_team_group = df_comb_player_team_group.sort_values('overall_rating').groupby('team_api_id').sum()
    df_top = pd.merge(df_comb_player_team_group,df_end_of_year_team,on="team_api_id")
    df_top = df_top[["team_api_id","overall_rating","team_long_name"]]
    df_top = df_top.sort_values("overall_rating")
    df_top = df_top[-n:]
    df_top = df_top.sort_values("overall_rating",ascending=False)
    return df_top

def league_to_team(df_match,year):
    df_match = df_match.loc[:,["date","league_id","home_team_api_id","away_team_api_id"]]
    df_match['date'] = pd.to_datetime(df_match['date'])
    df_match = df_match[df_match['date'].dt.year == year]
    df_match = df_match.drop('date',axis=1)
    df_match=df_match.melt(['league_id'])
    df_match = df_match.drop('variable',axis=1)
    df_match.rename( columns={"value":"team_api_id" },inplace=True)
    df_match = df_match.drop_duplicates()
    return df_match

def top_leagues(df_comb_team,df_comb_player,df_match,season="2015/2016"):
    year = int(season.split("/")[0])
    df_end_of_year_team = end_of_year_team(df_comb_team)
    df_end_of_year_player = end_of_year_player(df_comb_player,year)
    df_team_to_player = team_to_player(df_match,year)
    df_end_of_year_player = pd.merge(df_end_of_year_player, df_team_to_player, on="player_api_id")
    df_comb_player_team_group= df_end_of_year_player.sort_values('overall_rating').groupby('team_api_id').head(16)
    df_comb_player_team_group = df_comb_player_team_group.sort_values('overall_rating').groupby('team_api_id').sum()
    df_top = pd.merge(df_comb_player_team_group,df_end_of_year_team,on="team_api_id")
    df_top = df_top[["team_api_id","overall_rating","team_long_name"]]
    df_top = df_top.sort_values("overall_rating")
    df_top = df_top.sort_values("overall_rating",ascending=False)
    df_league_to_team = league_to_team(df_match,year)
    df_top = pd.merge(df_league_to_team,df_top,on="team_api_id")
    return df_top

def box_plot_leagues(df_comb_team,df_comb_player,df_match,df_league,season="2014/2015"):
    df = top_leagues(df_comb_team,df_comb_player,df_match,season=season)
    df = pd.merge(df,df_league,on="league_id")
    df_league.rename( columns={"id":"league_id" },inplace=True)
    df.sort_values("overall_rating")
    plt.figure(figsize=(10,10))
    my_palette = sns.color_palette("Paired", 11)
    ax = sns.boxplot(x="overall_rating", y="name", data=df,palette= my_palette)
    plt.title(season)
    plt.show()
    