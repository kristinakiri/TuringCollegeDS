from termcolor import colored
# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import fromstring, ElementTree

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
        
        
def value_counts_to_dataframe(df,col):
    """This function does the aggregation of dataset - counts values per selected dimension
    and calculates the proportion"""
    temp_df = df[col].value_counts().rename_axis(col).reset_index(name='counts')
    temp_df = temp_df.sort_values(by=[col])
    temp_df['proportion'] = round(temp_df.counts/len(df)*100,2)
    temp_df = temp_df.reset_index()
    temp_df.drop(columns=['index'],inplace=True)
    return temp_df

def pivot_dim2(df,col1,col2):
    """This function aggregates per 2 dimensions and returns value counts,
    and proportion per first dimension group
    """
    agg = (df.groupby([col1,col2])
            .agg(Occur=('CustomerId','count'))
            .reset_index())
    agg_tot = (df.groupby([col1])
            .agg(OccurTot=('CustomerId','count'))
            .reset_index())
    agg = pd.merge(agg,agg_tot,
                   how='left',
                   on=col1)
    agg['Share'] = round(agg.Occur/agg.OccurTot*100,2)
    return agg