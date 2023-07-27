# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:49:27 2023

@author: mhouts
"""

import pandas as pd
import sqlalchemy as sa

#------------------------------------------------------------------------------
#Extract block
#------------------------------------------------------------------------------

print("First copy the path to the file, with filename and extension included")

fileChoice = ""
while fileChoice != 1 and fileChoice != 2:
    fileChoice = int(input("Press 1 for xls file, or press 2 for a csv file:"))

if fileChoice == 2
try:
    #To see all rows
    pd.set_option('display.max_columns', None)
    
    #read the csv
    df = pd.read_csv('') # Paste the relative path to the desired file

except FileNotFoundError:
    print("The csv was not found or was in another format.")

#------------------------------------------------------------------------------
#Transformation block 
#------------------------------------------------------------------------------

#try:
    #write here your transformations for the excel or csv

#except:
    #print("Something went wrong in the transformation. Could be different columns, the format or missing data.")
    #print("Check your csv for the following columns: Year,Punxsutawney Phil,February Average Temperature,February Average Temperature (Northeast),February Average Temperature (Midwest),February Average Temperature (Pennsylvania),March Average Temperature,March Average Temperature (Northeast),March Average Temperature (Midwest),March Average Temperature (Pennsylvania)")

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