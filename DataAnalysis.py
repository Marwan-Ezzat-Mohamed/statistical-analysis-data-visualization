import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
from sklearn.linear_model import LinearRegression

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
plt.xlabel('Year', fontsize=18)
plt.ylabel('Unit Sales(in millions)', fontsize=16)
plt.plot(x, y, 'o')

#histogram
#plt.hist(x, "auto", ec = "black")
#plt.xlabel('Year', fontsize=18)
#plt.ylabel('Unit Sales(in millions)', fontsize=16)
#plt.title('Unit sales of the Apple iPhone worldwide from 2010 to 2018(in millions)', fontsize = 10)

#boxplot
#plt.boxplot(y , vert = False)

#plt.show()

df = df.sort_values(by='Unit Sales(in millions)').reset_index(drop=True)
df.head()
print(df)

#Measures of Central Tendency
#Mean = y.mean()
#print(Mean)
#Median = data.median()
#print(Median)
#Mode = y.mode()[0]
#print(Mode)

#MaxNum = y.max()
#print(MaxNum)
#MinNum = y.min()
#print(MinNum)

#Measures of Dispersion
#Range = MaxNum - MinNum
#print(Range)

#Regression Line
X = df.iloc[:, 0].values.reshape(-1, 1)
Y = df.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression()  
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

# scatter Graph
plt.scatter(X,Y)
plt.plot(X, Y_pred, color='red')

plt.show()