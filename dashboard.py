"""Week 4 client project: create visualizations for student performance data."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "student_performance.csv"
PLOTS = BASE / "plots"

def create_dashboard():
    data = pd.read_csv(DATA_FILE).dropna()
    PLOTS.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    plt.hist(data["Final_Score"], bins=6, edgecolor="black")
    plt.title("Distribution of Final Scores")
    plt.xlabel("Final Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(PLOTS / "histogram_final_scores.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=data, x="Hours_Studied", y="Final_Score")
    plt.title("Study Hours vs Final Score")
    plt.tight_layout()
    plt.savefig(PLOTS / "scatter_study_hours_vs_score.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 5))
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(PLOTS / "correlation_heatmap.png", dpi=150)
    plt.close()

    grid = sns.PairGrid(data)
    grid.map_diag(plt.hist, edgecolor="black")
    grid.map_offdiag(plt.scatter)
    grid.fig.suptitle("Pairplot: Student Performance Features", y=1.02)
    grid.savefig(PLOTS / "pairplot_student_performance.png", dpi=150)
    plt.close("all")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes[0, 0].hist(data["Final_Score"], bins=6, edgecolor="black")
    axes[0, 0].set_title("Final Score Distribution")
    axes[0, 0].set_xlabel("Final Score")
    axes[0, 0].set_ylabel("Students")
    sns.scatterplot(data=data, x="Hours_Studied", y="Final_Score", ax=axes[0, 1])
    axes[0, 1].set_title("Study Hours vs Final Score")
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", ax=axes[1, 0])
    axes[1, 0].set_title("Feature Correlations")
    sns.scatterplot(data=data, x="Attendance", y="Final_Score", ax=axes[1, 1])
    axes[1, 1].set_title("Attendance vs Final Score")
    fig.suptitle("Student Performance Analysis Dashboard", fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PLOTS / "student_performance_dashboard.png", dpi=160)
    plt.close(fig)
    print("Dashboard and plots saved in the plots folder.")

if __name__ == "__main__":
    create_dashboard()
