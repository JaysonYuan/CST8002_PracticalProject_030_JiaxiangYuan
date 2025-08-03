
import matplotlib.pyplot as plt
from collections import Counter

def generate_pie_chart(data, column):
    values = [record[column] for record in data if column in record]
    counts = Counter(values)

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"Distribution of {column}")
    plt.axis('equal')
    plt.savefig(f"{column}_pie_chart.png")
    plt.show()
