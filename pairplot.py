import seaborn
import matplotlib.pyplot as plt

df=seaborn.load_dataset('tips')
print(df)

#pairplot with hue sex
seaborn.pairplot(df, hue='sex')

#to show
plt.show()