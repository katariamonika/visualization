"""
Session 04: Visualization with purpose and accessible data visualization

This session focused on designing visualizations with a clear purpose
and applying accessibility principles so that visualizations are usable
by a wide audience.

Key ideas:
- Visualizations should be created with a specific audience and goal in mind
- Design choices are not neutral and affect interpretation
- Accessibility should be considered from the start
"""

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Reproducible data generation
# -----------------------------
# Set a random seed so results can be reproduced
np.random.seed(42)

x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

# -----------------------------
# Create a visualization with purpose
# -----------------------------
# Purpose: compare two groups clearly on the same axes

fig, ax = plt.subplots(figsize=(6, 4))

ax.scatter(x, y1, label="Group 1")
ax.scatter(x, y2, label="Group 2")

ax.set_title("Comparison of Two Groups Over Time")
ax.set_xlabel("Observation Index")
ax.set_ylabel("Value")

ax.legend(loc="lower right")

# -----------------------------
# Accessibility considerations
# -----------------------------
# - Clear labels and title
# - Legend included instead of relying only on color
# - Reasonable figure size for readability

# Add a short annotation to guide interpretation
ax.annotate(
    "Higher values indicate increased measurements",
    xy=(5, 90),
    ha="left"
)

plt.tight_layout()
plt.show()

"""
Notes:
- The visualization communicates a clear message rather than showing data without context
- Labels and legends reduce reliance on color alone
- A fixed random seed supports reproducibility
- Simple annotations help guide the viewer
"""
