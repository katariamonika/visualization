"""
Visualization — Live Learning Session 3
Date: 2026-01-22

Overview:
- This session focused on reproducible data visualization.
- We reviewed how visualizations communicate and persuade and how they reflect choices.
- We practiced making plots with multiple series and improving readability with labels legends and annotations.
- We also practiced removing tick marks and labels when they are not needed.

Notes:
- Reproducibility means someone else can run the same code and get the same results.
- Using a fixed random seed helps keep generated example data consistent.
- Visualizations are not neutral because we choose what to show and how to show it.
- Adding labels and a legend makes it easier to interpret multiple series.
- Annotations can highlight an important value or point in the plot.
- Removing ticks or tick labels can reduce clutter if they do not add meaning.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import NullLocator

np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

fig, ax = plt.subplots(figsize=(5, 3))

ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc="lower right")

ax.text(
    10,
    95,
    "This value is important!",
    ha="center",
    color="red",
    fontsize=14
)

ax.yaxis.set_major_locator(NullLocator())
ax.xaxis.set_major_formatter(NullFormatter())

ax.set_title("Reproducible scatter plot example")
plt.tight_layout()
plt.show()
