"""
Visualization— Live Learning Session 1
Date: 2026-01-15

Overview:
- Learned how to create a basic figure using matplotlib.
- Generated small sample data using NumPy.
- Created a simple scatter plot and confirmed it renders correctly.

Notes / takeaways:
- Using a fixed random seed helps make plots reproducible (same random values each run).
- plt.subplots() is a clean way to create a Figure + Axes object for plotting.
- Scatter plots are useful for showing relationships/patterns between two numeric variables.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Create sample data (reproducible) ---
np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100, 50)

# --- Make a basic scatter plot ---
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)

# Add minimal labeling for readability
ax.set_title("Basic scatter plot (Session 1)")
ax.set_xlabel("x (index)")
ax.set_ylabel("y (random integer 0–100)")

plt.tight_layout()
plt.show()
