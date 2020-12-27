import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

 

plt.style.use('bmh')

df = pd.read_csv('Access to Computers From Home.csv')

labels = ['Location']

df.groupby('Time')[labels]

 

# All Brands

#x = df['Location']

#y = df['Percentage of Households']

 

#Bar Chart

locations = ['DNK', 'DEU', 'ISL', 'JPN', 'FRA', 'HUN', 'POL', 'ESP', 'GRC', 'IRL', 'KOR', 'MEX', 'NOR', 'ITA']

indx = np.arange(len(locations))

percentage_label = np.arange(0, 100, 10)

perc_2007 = [82.960, 78.647, 89.150, 85.000, 65.549, 52.565, 53.689, 58.949, 40.167, 65.487, 80.447, 22.120, 82.417, 53.380]

perc_2017 = [93.137, 92.866, 97.297, 72.500, 84.125, 79.675, 81.777, 78.385, 70.500, 83.758, 74.708, 45.419, 94.906, 72.502]

bar_width = 0.35

fig, ax = plt.subplots()

bar2007 = ax.bar(indx - bar_width/2, perc_2007, bar_width, label = 'Year 2007')

bar2017 = ax.bar(indx + bar_width/2, perc_2017, bar_width, label = 'Year 2017')

ax.set_xticks(indx)

ax.set_xticklabels(locations)

 

ax.set_xlabel ('Locations')

ax.set_ylabel ('Percentage of Households(%)')

ax.set_title('Number of Households that have atleast one PC')

ax.legend()

 

#Pie Chart

#plt.pie(y, labels=x, radius=1.2,autopct='%0.01f%%', shadow=True, explode=[.05,.2,.05,.2,.05,.2,.05])

 

#Scatter Graph

#plt.xlabel('Model', fontsize=18)

#plt.ylabel('Price($)', fontsize=16)

#plt.scatter(x, y)

 

#Histogram

#plt.hist(y,"auto",ec="black")

#plt.xlabel('Price($)', fontsize=18)

#plt.ylabel('Count', fontsize=16)

#plt.title("Phone Prices")

 

#Boxplot

#plt.boxplot(y , vert = False)

 

plt.show()