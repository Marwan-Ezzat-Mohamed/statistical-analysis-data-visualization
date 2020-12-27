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

#Bar chart
#plt.xlabel('Year', fontsize=16)
#plt.ylabel('Unit Sales (in millions)', fontsize=16)
#plt.bar(x, y)

#Pie chart
#plt.title("Unit sales of the Apple iPhone worldwide from 2010 to 2018(in millions)", fontsize = 10)
#plt.pie(y, labels=x, radius=1.0,autopct='%0.01f%%', shadow=False, explode=(0.1,0,0,0,0,0.1,0,0,0))
#plt.axis('equal') #Assures it's a circle

#Scatter Graph
#plt.xlabel('Year', fontsize=18)
#plt.ylabel('Unit Sales(in millions)', fontsize=16)
#plt.plot(x, y, 'o')

#Regression
#X = df.iloc[:, :-1].values.reshape(-1, 1)
#print (X)
#Y = df.iloc[:, 1].values.reshape(-1, 1)
#linear_regressor = LinearRegression()  
#linear_regressor.fit(X, Y)
#Y_pred = linear_regressor.predict(X)

#Scatter Graph(With Regression Line)
#plt.scatter(X,Y)
#plt.plot(X, Y_pred, color='red')

#Histogram
#plt.hist(x, "auto", ec = "black")
#plt.xlabel('Year', fontsize=18)
#plt.ylabel('Unit Sales(in millions)', fontsize=16)
#plt.title('Unit sales of the Apple iPhone worldwide from 2010 to 2018(in millions)', fontsize = 10)

#Boxplot
#plt.boxplot(y , vert = False)

#plt.show()

#Measures of Central Tendency
Mean = y.mean()
print(Mean)
Median = y.median()
print(Median)
Mode = y.mode()[0]
print(Mode)

MaxNum = y.max()
print(MaxNum)
MinNum = y.min()
print(MinNum)

#Measures of Dispersion
Range = MaxNum - MinNum
print(Range)