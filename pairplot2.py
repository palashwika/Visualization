import seaborn
import matplotlib.pyplot as plt

df=seaborn.load_dataset('tips')

seaborn.pairplot(df, hue="day")

plt.show()