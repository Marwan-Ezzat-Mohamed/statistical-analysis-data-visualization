import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean
from sklearn.linear_model import LinearRegression

filename = 'Sales.csv'

#Titles for axes
xTitle = 'Year'
yTitle = 'Unit Sales(in millions)'

plt.style.use('bmh')
df = pd.read_csv(filename)

# All Brands
x = df[xTitle]
y = df[yTitle]


#Measures of Central Tendency
#Mean = y.mean()
#print("%.3f" % Mean)
#Median = y.median()
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

#Bar chart
#plt.xlabel(xTitle, fontsize=16)
#plt.ylabel(yTitle, fontsize=16)
#plt.bar(x, y)

#Pie chart
#plt.pie(y, labels=x, radius=1.0,autopct='%0.01f%%', shadow=False, explode=(0.1,0,0,0,0,0.1,0,0,0))
#plt.axis('equal') #Assures it's a circle

#Histogram
#plt.hist(x, "auto", ec = "black")
#plt.xlabel(xTitle, fontsize=18)
#plt.ylabel(yTitle, fontsize=16)

#Boxplot
#plt.boxplot(y , vert = False)

#Scatter Graph
#plt.xlabel(xTitle, fontsize=18)
#plt.ylabel(yTitle, fontsize=16)
#plt.plot(x, y, 'o')

#Regression
#X = df.iloc[:, :-1].values.reshape(-1, 1)
#Y = df.iloc[:, 1].values.reshape(-1, 1)
#linear_regressor = LinearRegression()  
#linear_regressor.fit(X, Y)
#Y_pred = linear_regressor.predict(X)

#Scatter Graph(With Regression Line)
#newX = [[2019], [2020], [2021]]
#newY = linear_regressor.predict(newX)
#print(newY)

#plt.scatter(X,Y,color='#003F72',label='Data')
#plt.plot(X, Y_pred, color = 'red',label='Regression line')
#plt.scatter(newX,newY, color = 'green', label='Prediction')
#plt.legend(loc=4)

plt.show()




