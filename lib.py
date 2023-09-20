import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from fpdf import FPDF


def readfile(filepath):
    return pd.read_csv(filepath)


# provides summary stats in a pdf file and graph, both in the output folder
def stats(df):
    print(df.describe())


def save_stats(df):
    # Generate the summary report
    summary_report = df.describe()

    # Format the summary report as a table
    summary_table = tabulate(summary_report, headers="keys")

    # Save the summary report to a PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=summary_table, align="C")
    pdf.output("output/summary_report.pdf")
    return summary_table


def visualize_cars(df):
    # Create the scatter plot
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df["mpg"], df["hp"], c="b", marker="o", edgecolors="k", alpha=0.6)
    plt.title("Scatter Plot of MPG vs. HP")
    plt.xlabel("MPG")
    plt.ylabel("HP")

    # Save the visualization as an image file
    plt.savefig("output/scatter_plot.png", dpi=300, bbox_inches="tight")

    # Display the plot (optional)
    plt.show()
    return fig
