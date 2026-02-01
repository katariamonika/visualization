"""
Visualization — Live Learning Session 2
Date: 2026-01-20

Overview:
- This session focused on understanding good and bad data visualization.
- We discussed how visualization choices depend on purpose audience and context.
- Examples were shown to compare effective and ineffective chart designs.

Notes:
- A good visualization makes the message easy to understand.
- A bad visualization increases confusion or can mislead the viewer.
- Design choices such as chart type labels color and scale matter.
- Bar charts are usually better for comparing values than pie charts.
- Too many colors effects or decorations reduce clarity.
- Accessibility includes readable labels good contrast and not relying only on color.
"""

import numpy as np
import matplotlib.pyplot as plt

# Sample data used to demonstrate different visualization choices
categories = ["A", "B", "C", "D", "E"]
values = [25, 40, 55, 30, 45]

# Clear example: bar chart
fig, ax = plt.subplots(figsize=(6, 3))
ax.bar(categories, values)
ax.set_title("Bar chart example")
ax.set_xlabel("Category")
ax.set_ylabel("Value")
plt.tight_layout()
plt.show()

# Less effective example: pie chart for comparison
fig, ax = plt.subplots(figsize=(5, 4))
ax.pie(values, labels=categories, autopct="%1.0f%%")
ax.set_title("Pie chart example")
plt.tight_layout()
plt.show()
