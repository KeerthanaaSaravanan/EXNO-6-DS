# -*- coding: utf-8 -*-
"""EX NO6:Data visualization Using Seaborn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A3nhw0cGQhMcJhxLw-OymOlkER_Ul3_S

**Data visualization Using Seaborn**
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Datas
x = [1, 2, 3, 4, 5]
y = [3, 6, 2, 7, 1]

# Create line plot using seaborn

x = [1, 2, 3, 4, 5]
y1 = [3, 5, 2, 6, 1]
y2 = [1, 6, 4, 3, 8]
y3 = [5, 2, 7, 1, 4]

# implement line plot and include all the necessary parameters

"""**Bar Plot - Seaborn**"""

tips = sns.load_dataset('tips')

# Implement Bar plot with hue parameter

# Set labels and title

# Include titanic dataset
tit=pd.read_csv("/content/titanic_dataset.csv")
tit

plt.figure(figsize=(8,5))
# Implement barplot using seaborn and set x='Embarked',y='Fare',data=tit, palette='rainbow' and set graph title as "Fare of Passenger by Embarked Town"

plt.figure(figsize=(8,5))
# Implement barplot using seaborn and set x='Embarked',y='Fare',data=tit, palette='rainbow',hue='Pclass' and set graph title as "Fare of Passenger by Embarked Town, Divided by Class"

import seaborn as sns
# using tips dataset implement Scatter plot of total bill vs tip amount

# Set labels and title
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.title('Scatter Plot of Total Bill vs. Tip Amount')

"""**VIOLIN PLOT**"""

# implement violinplot by comparing any two values from titanic data set

"""**HISTOGRAM**"""

import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(0)
marks = np.random.normal(loc=70, scale=10, size=100)

# Generating dataset of random numbers
np.random.seed(1)
num_var = np.random.randn(1000)
Name : Keerthana Saravanan
num_var

# IMPLEMENT HISTOGRAM

# IMPLEMENT histplot in seaborn and set parameters data=df,x=Pclass,hue=Survived,kde=True