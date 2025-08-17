"""
E-commerce Customer Retention: 2024 Trend vs Benchmark
Email (verification): 24f2008495@ds.study.iitm.ac.in

This script:
- Loads quarterly retention figures for 2024
- Computes the average (must be 71.74 as per prompt)
- Plots the quarterly trend with an industry benchmark line at 85
- Saves the plot to 'retention_trend.png'
"""
import matplotlib.pyplot as plt

# Quarterly data
quarters = ["Q1", "Q2", "Q3", "Q4"]
retention = [65.3, 70.94, 76.58, 74.14]
industry_target = 85.0

# Average (given/verified)
average = round(sum(retention) / len(retention), 2)
print(f"Computed average retention: {average}")  # Expect 71.74

# Plot
plt.figure(figsize=(8, 5))
plt.plot(quarters, retention, marker='o', linewidth=2)
plt.axhline(y=industry_target, linestyle='--', linewidth=2)
plt.title("Customer Retention Rate (2024) vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate")  # Interpreted as percentage points
for x, y in zip(quarters, retention):
    plt.text(x, y + 0.6, f"{y}", ha='center', va='bottom')
plt.text(quarters[-1], industry_target + 0.6, "Target: 85", ha='left', va='bottom')
plt.tight_layout()
plt.savefig("retention_trend.png", dpi=160, bbox_inches='tight')
print("Saved retention_trend.png")


# analysis.py
# Author: 24f2008495@ds.study.iitm.ac.in

import marimo as mo

# --- Cell 1: Import dataset and define variable ---
# This is our base dataset, which other cells depend on
data = {"x": list(range(1, 101)), "y": [i**2 for i in range(1, 101)]}


# --- Cell 2: Interactive widget ---
# The slider value will be used to dynamically filter data
slider = mo.ui.slider(1, 100, value=10)


# --- Cell 3: Compute dependent variable ---
# This cell depends on both 'data' and 'slider'
# It selects the first N values of y based on the slider
subset_y = data["y"][: slider.value]


# --- Cell 4: Dynamic Markdown Output ---
# This depends on 'subset_y' and 'slider'
mo.md(
    f"""
    ## Data Analysis Snapshot  
    Showing first **{slider.value}** values of y = x²  

    **Last Value in Subset:** {subset_y[-1]}  
    {"🟢" * (slider.value // 5)}
    """
)
