# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:07:08 2023

@author: mhouts
"""
import pandas as pd
import sqlalchemy as sa

#------------------------------------------------------------------------------
#Extract block
#------------------------------------------------------------------------------
try:
    #To see all rows
    pd.set_option('display.max_columns', None)
    
    #read the csv
    df = pd.read_csv('philsSightings.csv') 

except FileNotFoundError:
    print("The csv was not found or was in another format.")

#------------------------------------------------------------------------------
#Transformation block
#------------------------------------------------------------------------------

try:
    #Unpivot the month columns to rows
    df = df.melt(id_vars=['Year', 'Punxsutawney Phil'], var_name = 'RegionMonth', value_name='Average temperature') # unpivot the data
    
    #Split the column could also extract, may come later
    df[["Month", "Region"]] = df["RegionMonth"].str.split("(", expand=True)
    
    #Remove  the ) at the end of region
    df['Region'] = df['Region'].str.replace(')','')
    
    #Remove the splitted column
    df = df.drop('RegionMonth', axis=1)
    
    # It's alwasy in February, so month is redunded
    df = df.drop('Month', axis=1)
    
    # Add the groundhog day to the year
    df['Year'] = df.Year.map(str) + "-02-02"
    
    # Drop all empty or incomplete predictions
    df = df.dropna()

except:
    print("Something went wrong in the transformation. Could be different columns, the format or missing data.")
    print("Check your csv for the following columns: Year,Punxsutawney Phil,February Average Temperature,February Average Temperature (Northeast),February Average Temperature (Midwest),February Average Temperature (Pennsylvania),March Average Temperature,March Average Temperature (Northeast),March Average Temperature (Midwest),March Average Temperature (Pennsylvania)")

#------------------------------------------------------------------------------
#Load block
#------------------------------------------------------------------------------

try:
    #connection String
    engine = sa.create_engine('mssql+pyodbc://localhost/groundhogdb?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
    connection = engine.connect()
    
    #Make table and load dataframe into database
    df.to_sql('Predictions', engine, if_exists='replace')
    
    #Make a select query to test the inserted data
    query = sa.text("SELECT * FROM Predictions")
    result = connection.execute(query)
    
    # Fetch the result rows
    rows = result.fetchall()
    
    # Process the result
    for row in rows:
        print(row)
    
    # Close the connection
    connection.close()

except TypeError:
    print("Something wrong with sql. It's probably the connection, but you never know.")