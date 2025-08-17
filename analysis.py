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
