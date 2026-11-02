#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Upload File


#Load dataset
HouseDF = pd.read_csv("USA_Housing (1).csv")

#Display first few rows
print(HouseDF.head())

#Dataset information
print(HouseDF.info())

#Statistical summary
print(HouseDF.describe())

#Column names
print(HouseDF.columns)

#Pairplot for numerical features
print(sns.pairplot(HouseDF))

#Correlation heatmap
plt.figure(figsize=(8,6))

sns.heatmap(HouseDF.corr(), annot=True)

plt.title("Correlation Heatmap")
plt.show()