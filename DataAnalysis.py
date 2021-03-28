import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean
from sklearn.linear_model import LinearRegression
from tkinter import *
import math
from PIL import ImageTk,Image 
filename = 'Sales.csv'
import tkinter.font as tkFont



plt.style.use('bmh')
df = pd.read_csv(filename)

# Titles for axes

xTitle = df.columns[0]
yTitle = df.columns[1]

# All Brands
x = df[xTitle]
y = df[yTitle]

sqrtDataSetSize = math.ceil(math.sqrt(x.size))

# Measures of Central Tendency
# Mean = y.mean()
# print("%.3f" % Mean)
# Median = y.median()
# print(Median)
# Mode = y.mode()[0]
# print(Mode)

#MaxNum = y.max()
# print(MaxNum)
#MinNum = y.min()
# print(MinNum)

# Measures of Dispersion
#Range = MaxNum - MinNum
# print(Range)

root = Tk()
root.geometry("360x620")
root.resizable(False, False)
root.configure(background = '#051626')
fontStyle = tkFont.Font(family="verdanab", size=30)
fontValues=tkFont.Font(family="verdanab", size=16)
#Images
BarImage = PhotoImage(file = 'barImage.png')
PieImage = PhotoImage(file = 'pieImage.png')
HistogramImage = PhotoImage(file = 'histogramImage.png')
ScatterPlotImage = PhotoImage(file = 'scatterPlotImage.png')
BoxPlotImage = PhotoImage(file = 'boxPlotImage.png')
ScatterRegressionImage = PhotoImage(file = 'scatterRegressionImage.png')
MeanImage = PhotoImage(file = 'meanImage.png')
MedianImage = PhotoImage(file = 'medianImage.png')
ModeImage = PhotoImage(file = 'modeImage.png')

GraphsLabel=Label(root,text="Graphs",bg='#051626',fg='white',font=fontStyle)
GraphsLabel.place(x=10,y=40)


# Bar chart
def BarChartGraph():
    plt.xlabel(xTitle, fontsize=16)
    plt.ylabel(yTitle, fontsize=16)
    plt.bar(x, y)
    plt.show()


BarButton = Button(root,width=100,command=BarChartGraph,highlightthickness = 0, bd = 0,bg='#051626',image=BarImage,activebackground='#051626')           

BarButton.place(x=10,y=120)



# Pie chart


def PieChartGraph():
    plt.pie(y, labels=x, radius=5, autopct='%1.1f%%',pctdistance=0.8,labeldistance=1.07,startangle=40)     
    plt.axis('equal')  # Assures it's a circle
    plt.aspect=1
    plt.show()


PieButton = Button(root,width=100,command=PieChartGraph,highlightthickness = 0, bd = 0,bg='#051626',image=PieImage,activebackground='#051626')           

PieButton.place(x=130,y=120)


# Histogram


def HistogramGraph():
    plt.hist(y, bins=int(sqrtDataSetSize), ec="black")
    plt.xlabel(xTitle, fontsize=18)
    plt.ylabel(yTitle, fontsize=16)
    plt.show()


HistogramButton = Button(root,width=100,command=HistogramGraph,highlightthickness = 0, bd = 0,bg='#051626',image=HistogramImage,activebackground='#051626')               
HistogramButton.place(x=250,y=120)


# Boxplot


def BoxplotGraph():
    plt.boxplot(y, vert=False)
    plt.show()


BoxplotButton = Button(root,width=100,command=BoxplotGraph,highlightthickness = 0, bd = 0,bg='#051626',image=BoxPlotImage,activebackground='#051626')
BoxplotButton.place(x=10,y=260)

# Scatter Graph


def ScatterPlotGraph():
    plt.xlabel(xTitle, fontsize=18)
    plt.ylabel(yTitle, fontsize=16)
    plt.plot(x, y, 'o')
    plt.show()


ScatterPlotButton = Button(root,width=100,command=ScatterPlotGraph,highlightthickness = 0, bd = 0,bg='#051626',image=ScatterPlotImage,activebackground='#051626')                
ScatterPlotButton.place(x=130,y=260)
# RegressionLine


def RegressionLine():
    X = df.iloc[:, :-1].values.reshape(-1, 1)
    Y = df.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    # Scatter Graph(With Regression Line)
    newX = [[2019], [2020], [2021]]
    newY = linear_regressor.predict(newX)
    print(newY)
    plt.scatter(X, Y, color='#003F72', label='Data')
    plt.plot(X, Y_pred, color='red', label='Regression line')
    plt.scatter(newX, newY, color='green', label='Prediction')
    plt.legend(loc=4)
    plt.show()


ScatterRegressionButton = Button(root,width=100,highlightthickness = 0, bd = 0,bg='#051626',image=ScatterRegressionImage,activebackground='#051626' , command=RegressionLine)
ScatterRegressionButton.place(x=250,y=260)
ValuesLabel=Label(root,text="Values",bg='#051626',fg='white',font=fontStyle)
ValuesLabel.place(x=15,y=420)
def CalculateMean():
    Mean = y.mean()
    var1.set(round(Mean, 2))
    
    
var1=StringVar()
MeanLabel = Label(root,width=100,highlightthickness = 0, bd = 0,bg='#051626',image=MeanImage,activebackground='#051626')
MeanLabel.place(x=30,y=550)
CalculateMean()
MeanValueLabel =Label(root,textvariable=var1,bg='#051626',fg='white' ,font=fontValues) 
MeanValueLabel.place(x=45,y=500)


def CalculateMedian():
    Median = y.median()
    var2.set(round(Median, 2))

var2=StringVar()
MeadianLabel = Label(root,width=100,highlightthickness = 0, bd = 0,bg='#051626',image=MedianImage,activebackground='#051626')
MeadianLabel.place(x=135,y=550)
CalculateMedian()
MedianValueLabel =Label(root,textvariable=var2,bg='#051626',fg='white', font=fontValues) 
MedianValueLabel.place(x=150,y=500)

def CalculateMode():
    Mode = y.mode()
    var3.set(Mode[0])

var3=StringVar()
ModeLabel = Label(root,width=100, highlightthickness = 0, bd = 0,bg='#051626',image=ModeImage,activebackground='#051626')
ModeLabel.place(x=240,y=550)
CalculateMode()
ModeValueLabel =Label(root,textvariable=var3,bg='#051626',fg='white',font=fontValues ) 
ModeValueLabel.place(x=256,y=500)
root.mainloop()


