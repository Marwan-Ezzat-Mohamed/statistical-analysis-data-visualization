import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
from collections import Counter

plt.style.use('bmh')
df = pd.read_csv('Sales.csv')

# All Brands
x = df['Year']
y = df['Unit Sales(in millions)']

# Bar chart
#plt.xlabel('Year', fontsize=18)
#plt.ylabel('Unit Sales (in millions)', fontsize=16)
#plt.bar(x, y)

# Pie chart
#plt.title("Unit sales of the Apple iPhone worldwide from 2010 to 2018(in millions)", fontsize = 10)
#plt.pie(y, labels=x, radius=1.0,autopct='%0.01f%%', shadow=False, explode=None)

# scatter Graph
#plt.xlabel('Year', fontsize=18)
#plt.ylabel('Unit Sales(in millions)', fontsize=16)
#plt.plot(x, y, 'x')

#histogram
#plt.hist(x, "auto", ec = "black")
#plt.xlabel('Year', fontsize=18)
#plt.ylabel('Unit Sales(in millions)', fontsize=16)
#plt.title('Unit sales of the Apple iPhone worldwide from 2010 to 2018(in millions)', fontsize = 10)

#boxplot
#plt.boxplot(y , vert = False)

#plt.show()

#Measures of Central Tendency
Mean = y.mean()
print(Mean)
Median = y.median()
print(Median)
Mode = y.mode()[0]
print(Mode)

#Measure of Dispersion
#Range = y.statistics.range
#print(Range)