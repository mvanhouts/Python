# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:19:28 2023

@author: mhouts
"""

import pandas as pd
import sqlalchemy as sa

try:
    
    pd.set_option('display.max_columns', None) #To see all rows
    
    
    df = pd.read_csv('sales.csv') #read the csv

except FileNotFoundError:
    print("The csv was not found or was in another format.") 
    
    
df = df.rename(columns={"product_id": "product", "customer_id": "customer"}) #rename the columns

productAgg = df.groupby(["product"])["quantity","price"].sum() #group and sum the quantity and price
productAgg = productAgg.reset_index() #give an index to the groupby per item

dayAgg = df.groupby(["timestamp"])["price"].sum() #groupby for price per day
dayAgg = dayAgg.reset_index() #give an index


customerAgg = df["customer"].nunique() #C=count number of unique customers
customerAgg = pd.DataFrame([customerAgg], columns=['customernumber']) #set into dataframe for slqalchemy


#------------------------------------------------------------------------------
#Load block
#------------------------------------------------------------------------------

try:
    #connection String
    engine = sa.create_engine('mssql+pyodbc://localhost/pandasDumpDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
    connection = engine.connect()
    
    
    df.to_sql('sales', engine, if_exists='replace') #Make table and load dataframe into database
    
    productAgg.to_sql('producttotals', engine, if_exists='replace') #dataframe to sql
    
    dayAgg.to_sql('daytotals', engine, if_exists='replace')
    
    customerAgg.to_sql('customertotal', engine, if_exists='replace')
    

except TypeError: #error handling
    print("Something wrong with sql. It's probably the connection, but you never know.")