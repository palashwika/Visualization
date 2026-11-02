import matplotlib.pyplot as plt
import numpy as np

#Set random seed for reproductibility
np.random.seed(42)

#Generate dummy data: 50 days of ad spend vs revenue
ad_spend = np.random.uniform(100,1000,50)
#Revenue loosely equals 5 * ad_spend + base noise + a few high-return outliers
revenue = 5*ad_spend+np.random.normal(0,400,50)

plt.figure(figsize=(8, 5))
plt.scatter(ad_spend, revenue, color='teal', alpha=0.7, edgecolors ='black', label='Daily Data')

#Add a line of best fit
m, b = np.polyfit(ad_spend, revenue, 1)
plt.plot(ad_spend, m*ad_spend + b, color='coral', linewidth=2, label='Trend Line')

plt.title('Daily Ad Spend vs. Store Revenue', fontsize=12, fontweight='bold')
plt.xlabel('Ad Spend ($)')
plt.ylabel('Revenue ($)')
plt.legend()

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()