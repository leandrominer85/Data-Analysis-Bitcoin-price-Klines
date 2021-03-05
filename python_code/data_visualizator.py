#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import pandas as pd
import glob
import os


# In[12]:


def data_vis(path = '..\data\cleaned'):
    
    
    '''
    This function receives a path for the data. First it asks the user wich file(complete path) he wants.
    Uses this to load the dataframe. Then ask the dates for creating the graphs. Wich is used to create a filtered
    dataframe that feeds the Candestick graph
    
    Input:
    path - str; the path to the original data 
    
    
    Output:
    Interactive candestick graph.
    
    '''
    
    
    
    
    
    #Uses glob to get the list of files
    path = path
    files = glob.glob(path + "/*.csv")
    
    print("Select one of the data:")
    for i in files:
        print(i)
        
    #fet the file path
    file_path = input("File path")
    
    df = pd.read_csv(file_path, index_col="date")
    print()
    print("Select a date between {} and {}".format(df.index.min(), df.index.max()))
    print()
    
    
    #get the dates
    init_date = input("Begin date (format : year-month-day hour:min:sec). Ex: '2020-02-19 17:30:00'")
    final_date = input("Final date (format : year-month-day hour:min:sec). Ex: '2020-02-19 17:30:00'")
    
    
    #drop the unused column and filter the data
    df.drop("Unnamed: 0",axis=1, inplace=True)
    df2 = df[init_date:final_date]
    
    #get all fundings rates for the date range
    fundings = ["Funding Rate: {}".format(i) for i in df2["fundingRate"].values]
    

    #plot the graph
    fig = go.Figure(data=[go.Candlestick(x=df2.index,
                    open=df2['open'], high=df2['high'],
                    low=df2['low'], close=df2['close'], text =fundings)
                         ])




    fig.show()
    
    
    
    
    
    


# In[13]:


data_vis()


# In[ ]:





# In[ ]:




