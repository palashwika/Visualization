import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Set style for clean visuals
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1,2, figsize=(15,6))

#Example 1: restaurant avergae trap

np.random.seed(42)
#normal mea
lunch_rush = np.random.normal(loc=15, scale=5, size=500)

dinner_crowd = np.random.normal(loc=75, scale=10, size=500)
stay_times=np.concatenate([lunch_rush, dinner_crowd])

df_restaurant = pd.DataFrame({"Minutes": stay_times})
print(df_restaurant)
avg_time = df_restaurant["Minutes"].mean()
print(avg_time)


sns.histplot(data=df_restaurant, x="Minutes", bins=40, color="teal", alpha=0.7, ax=axes[0])

axes[0].axvline(avg_time, color='red', linestyle="--", linewidth=2.5, label=f"Calculated Average ({avg_time:.1f} min)")

axes[0].set_title("1. The Restaurant 'Average' Trap\n (Novody actually stays for 45 minutes)")
axes[0].set_xlabel("Time Spent in Restaurant (Minutes)")
axes[0].legend()

#RIGGED SYSTEM
natural_grades=np.random.normal(loc=52, scale=8, size=2000)

#Simulate teachers bumping anyone with a 46-49 up to a passing grade of 50
rigged_grades = np.where((natural_grades>=45)&(natural_grades<50), 50, natural_grades)

#Clip final scores to valid exam bound
rigged_grades=np.clip(rigged_grades, 0, 100)
df_grades=pd.DataFrame({"Final Score": rigged_grades})

#Plot Rigged Grades Data
sns.histplot(data=df_grades, x="Final Score", bins=50, color="crimson", alpha=0.7, ax=axes[1])
axes[1].axvline(50, color="black", linestyle=":", linewidth=2, label="Passing Threshold (50)")

axes[1].set_title("2. The 'Rigged' Grade System\n(Unnatural spike at 50 proves human intervention)", fontsize=13, pad=10)

axes[1].set_xlabel("Exam Score(0-100)")
axes[1].set_ylabel("Number of Students")
axes[1].set_xlim(25,75)
axes[1].legend()

plt.tight_layout()
plt.show()
