import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('brain_networks', header=[0, 1, 2], index_col=0)
df_subset = df.iloc[:, :4]

sns.pairplot(df_subset, kind="reg", diag_kind="kde")
plt.show()

print(df)



