"""
pie_chart.py
Generate a pie chart based on milk radiation dataset by province.

Author: Jiaxiang Yuan
"""

import matplotlib.pyplot as plt
from collections import defaultdict

def generate_pie_chart(data: list):
    """
    Generate a pie chart showing the number of records per province.
    
    Parameters:
        data (list): A list of dictionaries, each containing a 'province' key.
    """
    # Count the number of records per province
    province_counts = defaultdict(int)
    for record in data:
        province = record.get("province", "Unknown")
        province_counts[province] += 1

    labels = list(province_counts.keys())
    sizes = list(province_counts.values())

    # Generate pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Milk Radiation Records by Province")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
