"""
pie_chart.py
Generate a pie chart based on milk radiation dataset by user-selected field.

Author: Jiaxiang Yuan
"""

import matplotlib.pyplot as plt
from collections import defaultdict

def generate_pie_chart(data: list, column_name: str = "province"):
    """
    Generate a pie chart showing the distribution of values in the specified column.

    Parameters:
        data (list): A list of dictionaries containing the dataset records.
        column_name (str): The column to group by for pie chart (e.g., 'province', 'station').

    Returns:
        None. Displays a pie chart using matplotlib.
    """
    value_counts = defaultdict(int)
    for record in data:
        key = record.get(column_name, "Unknown")
        value_counts[key] += 1

    labels = list(value_counts.keys())
    sizes = list(value_counts.values())

    if not sizes or sum(sizes) == 0:
        print(f"[WARNING] No data found for column '{column_name}'. Cannot generate chart.")
        return

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"Milk Radiation Records by {column_name.capitalize()}")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
