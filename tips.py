import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import seaborn as sns
import pandas as pd

# Your original code will now work:
df = sns.load_dataset('tips')
df['final_bill'] = df['total_bill'] + df['tip']
print(df.head())



#barplot daywise earning
