import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Read datta from CSV file
df=pd.read_csv("country_vaccinations.csv")

#display first 10 rows
print(df.head(10))

#check for null values in each column; prints boolean values
print(df.isnull().any())

#Visualize missing values using a heatmap (optimize by ysing a subset of data)
subset=df.iloc[:5200, :] #first 100 rows for better performaces
plt.figure(figsize=(12,8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

#Display the first 10 rows
print(df.head(10))
#Drop rows where all values are NaN
print(df.dropna(how="all"))

#Fill missing values using backward fill method
print(df.bfill())

#Interpolate missing values
#print(df.interpolate())

#drop all rows with Nan values
print(df.dropna())
