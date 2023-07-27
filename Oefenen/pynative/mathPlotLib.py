# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:23:56 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Read Total profit of all months and show it using a line plot
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x_axis = df['month_number']
y_axis = df['total_profit']

plt.plot(x_axis,y_axis)
plt.title('Company profit per month')
plt.xlabel('Month number')
plt.ylabel('Profit')
plt.xticks(x_axis)
plt.show()

#------------------------------------------------------------------------------
# Exercise 2 Get total profit of all months and show line plot with the following Style properties
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x_axis = df['month_number']
y_axis = df['total_profit']

plt.plot(x_axis,y_axis,color='red', linestyle='dotted', linewidth=3, marker='o', mfc='black')
plt.title('Company Sales data of last year')
plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.legend(['Profit data last year'], loc='lower right')
plt.xticks(x_axis)
plt.show()

#------------------------------------------------------------------------------
# Exercise 3 Read all product sales data and show it  using a multiline plot
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

print(df)

x_axis = df['month_number']
plt.plot(x_axis, df['facecream'], marker='o', linestyle='-', color='b', label='Face Cream')
plt.plot(x_axis, df['facewash'], marker='o', linestyle='-', color='g', label='Face Wash')
plt.plot(x_axis, df['toothpaste'], marker='o', linestyle='-', color='r', label='Toothpaste')
plt.plot(x_axis, df['bathingsoap'], marker='o', linestyle='-', color='c', label='Bathing Soap')
plt.plot(x_axis, df['shampoo'], marker='o', linestyle='-', color='m', label='Shampoo')
plt.plot(x_axis, df['moisturizer'], marker='o', linestyle='-', color='y', label='Moisturizer')
plt.title('Sales data')
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(x_axis)
plt.show()

#------------------------------------------------------------------------------
# Exercise 4 Read toothpaste sales data of each month and show it using a scatter plot
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x_axis = df['month_number']
y_axis = df['toothpaste']

plt.scatter(x_axis,y_axis)
plt.title('Tooth paste Sales data')
plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.legend(['Profit data last year'], loc='lower right')
plt.xticks(x_axis)
plt.grid()
plt.show()

print(df)

#------------------------------------------------------------------------------
# Exercise 5 Read face cream and facewash product sales data and show it using the bar chart
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x_axis = df['month_number']

plt.figure(figsize=(10, 6))

bar_width = 0.35

bar_positions_facecream = x_axis
bar_positions_facewash = x_axis + bar_width

plt.bar(bar_positions_facecream, df['facecream'], width=bar_width, label='Face Cream')
plt.bar(bar_positions_facewash, df['facewash'], width=bar_width, label='Face Wash')

plt.title('Face Cream and Face Wash Sales Data')
plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.legend()
plt.xticks(x_axis)
plt.grid(True)
plt.show()

print(df)

#------------------------------------------------------------------------------
# Exercise 6 Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x_axis = df['month_number']
y_axis = df['bathingsoap']

plt.bar(x_axis,y_axis)
plt.title('Bathingsoap Sales data')
plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.legend(['bathingsoap sales data'], loc='lower right')
plt.xticks(x_axis)
plt.grid()
plt.savefig('bathingsoap.png',dpi=150)
plt.show()

print(df)

#------------------------------------------------------------------------------
# Exercise 7 Read the total profit of each month and show it using the histogram to see the most common profit ranges
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

y_axis = df['total_profit']
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]

plt.hist(y_axis,profit_range, label = 'Profit data')
plt.title('Profit data')
plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.legend(['Profit data'], loc='upper left')
plt.grid()
plt.savefig('bathingsoap.png',dpi=150)
plt.show()

print(df)

#------------------------------------------------------------------------------
# Exercise 8 Calculate total sale data for last year for each product and show it using a Pie chart
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')
df = df.sum()
df = df.drop('month_number')
df = df.drop('total_units')
df = df.drop('total_profit')
print(df)

dfLabels = df.index
x_axis = df

plt.pie(x_axis,autopct='%1.1f%%',labels=dfLabels)
plt.title('Sales data')
plt.legend(loc='lower right')
plt.show()

#------------------------------------------------------------------------------
# Exercise 9 Read Bathing soap facewash of all months and display it using the Subplot
#------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x_axis = df['month_number']
y_axis1 = df['bathingsoap']
y_axis2 = df['facewash']

plt.subplot(2,1,1)
plt.plot(x_axis,y_axis1,color='black',marker='o')
plt.title('Sales data Bathingsoap')
plt.xticks(x_axis)

plt.subplot(2,1,2)
plt.plot(x_axis,y_axis2,color='red',marker='o')
plt.title('Sales data Facewash')
plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.xticks(x_axis)
plt.show()


