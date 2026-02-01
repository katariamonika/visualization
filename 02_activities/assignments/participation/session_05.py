"""
Session 5 (260129) Participation
Topic: Subplots and combining visualizations plus wrapping up remaining coding topics

Key ideas
- Use subplots to compare views side by side when it supports the message
- Use layout tools so labels and titles do not overlap
- Save figures with a stable file name for reproducibility
- Combine plot types in one figure when the relationship is meaningful
- Reminder from class: check paths and dependencies early when running scripts
"""

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)

x = np.arange(50)
y_line = np.random.randint(10, 80, size=50)

names = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji"]
scores = [110, 180, 240, 100, 220]

fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y_line)
ax.set_title("Line chart example")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
fig.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(7, 3))
ax.bar(names, scores)
ax.set_title("Bar chart example")
ax.set_xlabel("Character")
ax.set_ylabel("Score")
fig.tight_layout()
plt.show()


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

axes[0].scatter(x, y_line)
axes[0].set_title("Scatter view")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Value")

axes[1].bar(names, scores)
axes[1].set_title("Bar view")
axes[1].set_xlabel("Character")
axes[1].set_ylabel("Score")

fig.tight_layout()
plt.show()


layout = [["A", "B"], ["C", "C"]]
fig, axd = plt.subplot_mosaic(layout, figsize=(10, 6), constrained_layout=True)

axd["A"].scatter(x, y_line)
axd["A"].set_title("A: Scatter")

axd["B"].plot(x, y_line)
axd["B"].set_title("B: Line")

axd["C"].bar(names, scores)
axd["C"].set_title("C: Bar (wide)")

plt.show()


fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y_line)
ax.set_title("Saving a figure")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
fig.tight_layout()

output_path = "session_05_saved_plot.png"
fig.savefig(output_path, dpi=300)
plt.show()

print(f"Saved figure to: {output_path}")
