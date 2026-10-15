import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Defin target parameter and size to test
mean, std = 175,7
sizes =[50,500,50000]
x=np.linspace(mean-4*std, mean+4*std,200)

fig, axes=plt.subplots(1,3,figsize=(15,4), sharey=True)

for ax,n in zip(axes, sizes):
    data = np.random.normal(mean,std,n)

    ax.hist(data, bins=30, density=True, alpha=0.5, color='teal', edgecolor="white")
    ax.plot(x, norm.pdf(x, mean, std), color='darkred', linewidth=2)

    ax.set_title(f"Sample Size: N = {n:,}")
    ax.set_xlabel("Height (cm)")
    if ax == axes[0]:ax.set_ylabel("Probability Density")

plt.tight_layout()
plt.show()