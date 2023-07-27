# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:49:42 2023

@author: mhouts
"""

#    Total number of log entries.
#    Total number of unique IP addresses.
#    The most frequent IP address.
#    The least frequent IP address.
#    The average response time.
#    The minimum response time.
#    The maximum response time.
#    The count of each unique status code.

import pandas as pd
try:        
    df = pd.read_csv("logFile.csv") #csv reader
except FileNotFoundError:
    print("File not found")
    raise

try:
    numberLogs = len(df.index) #count number of entries
    uniqueIP = df['ip_address'].nunique() # unique number of ip's
    mostFrequent = df['ip_address'].mode()[0] # mode is highest count of ID's and only the first entry of mode
    value_counts = df['ip_address'].value_counts() # get the counts of each ip entry
    leastFrequent = value_counts[value_counts == value_counts.min()].index[0] # minimal value from value counts
    avgResponse = df['response_time'].sum() / numberLogs # average is summing times / number of entries
    minResponse = df['response_time'].min() # minimal response time
    maxResponse = df['response_time'].max() # maximum response time
    countStatus = df['status_code'].value_counts() # counts per item in status
except:
    raise

try: 
    print("Total number of log entries: ",numberLogs) #printing all values in structured way
    print("Total number of unique IP addresses: ",uniqueIP)
    print("The most frequent IP address: ",mostFrequent)
    print("The least frequent IP address : ",leastFrequent)
    print("The average response time: ",avgResponse)
    print("The minimum response time: ",minResponse)
    print("The maximum response time: ",maxResponse)
    print("The count of each unique status code: \n",countStatus)
except:
    raise