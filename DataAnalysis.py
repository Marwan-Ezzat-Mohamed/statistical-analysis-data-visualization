import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean
from sklearn.linear_model import LinearRegression
from tkinter import *

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
# Mean = y.mean()
# print("%.3f" % Mean)
# Median = y.median()
# print(Median)
# Mode = y.mode()[0]
# print(Mode)

#MaxNum = y.max()
#print(MaxNum)
#MinNum = y.min()
#print(MinNum)

#Measures of Dispersion
#Range = MaxNum - MinNum
#print(Range)

root = Tk()
root.geometry("400x400")
#Bar chart
def BarChartGraph():
    plt.xlabel(xTitle, fontsize=16)
    plt.ylabel(yTitle, fontsize=16)
    plt.bar(x, y)
    plt.show()
button1 = Button(root,text="click to see the bar chart",command=BarChartGraph)   
button1.pack()
 
#Pie chart
def PieChartGraph():
    plt.pie(y, labels=x, radius=1.0,autopct='%0.01f%%', shadow=False, explode=(0.1,0,0,0,0,0.1,0,0,0))
    plt.axis('equal') #Assures it's a circle
    plt.show() 
button2 = Button(root,text="click to see the Pie chart",command=PieChartGraph)   
button2.pack()

#Histogram
def HistogramGraph():
    plt.hist(x, "auto", ec = "black")
    plt.xlabel(xTitle, fontsize=18)
    plt.ylabel(yTitle, fontsize=16)
    plt.show()
button3 = Button(root,text="click to see the Histogram ",command=HistogramGraph)   
button3.pack()

#Boxplot
def BoxplotGraph():
    plt.boxplot(y , vert = False)
    plt.show()
button4 = Button(root,text="click to see the box plot ",command=BoxplotGraph)   
button4.pack()

#Scatter Graph
def ScatterPlotGraph():
    plt.xlabel(xTitle, fontsize=18)
    plt.ylabel(yTitle, fontsize=16)
    plt.plot(x, y, 'o')
    plt.show()
button5 = Button(root,text="click to see the Scatter plot ",command=ScatterPlotGraph)   
button5.pack()
#RegressionLine
def RegressionLine():
    X = df.iloc[:, :-1].values.reshape(-1, 1)
    Y = df.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()  
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    #Scatter Graph(With Regression Line)
    newX = [[2019], [2020], [2021]]
    newY = linear_regressor.predict(newX)
    print(newY)
    plt.scatter(X,Y,color='#003F72',label='Data')
    plt.plot(X, Y_pred, color = 'red',label='Regression line')
    plt.scatter(newX,newY, color = 'green', label='Prediction')
    plt.legend(loc=4)
    plt.show() 
button6 = Button(root,text="click to see the Scatter Graph with Regression line ",command=RegressionLine)   
button6.pack()  
def CalculateMean():
    Mean = y.mean()
    print("%.3f" % Mean)
    plt.show()
button7 = Button(root,text="click to Calculate Mean ",command=CalculateMean)   
button7.pack()
def CalculateMedian():
    Median = y.median()
    print(Median)
    plt.show()
button8 = Button(root,text="click to Calculate Median ",command=CalculateMedian)   
button8.pack()
def CalculateMode():
    Mode = y.mode()[0]
    print(Mode)
    plt.show()
button9 = Button(root,text="click to Calculate Mode ",command=CalculateMode)   
button9.pack()
root.mainloop()












