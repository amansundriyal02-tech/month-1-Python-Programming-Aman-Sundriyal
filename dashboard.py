"""Create plots and a dashboard for student performance data."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "student_performance.csv"
PLOTS = BASE / "plots"
REQUIRED_COLUMNS = {"Hours_Studied", "Attendance", "Previous_Score", "Final_Score"}


def create_dashboard():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    data = pd.read_csv(DATA_FILE)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {', '.join(sorted(missing))}")

    for column in REQUIRED_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data = data.dropna(subset=list(REQUIRED_COLUMNS))
    if data.empty:
        raise ValueError("No valid student records available for plotting.")

    PLOTS.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data["Final_Score"], bins=6, edgecolor="black")
    ax.set(title="Distribution of Final Scores", xlabel="Final Score", ylabel="Number of Students")
    fig.tight_layout()
    fig.savefig(PLOTS / "histogram_final_scores.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=data, x="Hours_Studied", y="Final_Score", ax=ax)
    ax.set(title="Study Hours vs Final Score", xlabel="Hours Studied", ylabel="Final Score")
    fig.tight_layout()
    fig.savefig(PLOTS / "scatter_study_hours_vs_score.png", dpi=150)
    plt.close(fig)

    numeric = data.select_dtypes(include="number")
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    fig.tight_layout()
    fig.savefig(PLOTS / "correlation_heatmap.png", dpi=150)
    plt.close(fig)

    grid = sns.PairGrid(data)
    grid.map_diag(plt.hist, edgecolor="black")
    grid.map_offdiag(plt.scatter)
    grid.fig.suptitle("Pairplot: Student Performance Features", y=1.02)
    grid.savefig(PLOTS / "pairplot_student_performance.png", dpi=150)
    plt.close(grid.fig)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes[0, 0].hist(data["Final_Score"], bins=6, edgecolor="black")
    axes[0, 0].set(title="Final Score Distribution", xlabel="Final Score", ylabel="Students")
    sns.scatterplot(data=data, x="Hours_Studied", y="Final_Score", ax=axes[0, 1])
    axes[0, 1].set_title("Study Hours vs Final Score")
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", ax=axes[1, 0])
    axes[1, 0].set_title("Feature Correlations")
    sns.scatterplot(data=data, x="Attendance", y="Final_Score", ax=axes[1, 1])
    axes[1, 1].set_title("Attendance vs Final Score")
    fig.suptitle("Student Performance Analysis Dashboard", fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PLOTS / "student_performance_dashboard.png", dpi=160)
    plt.close(fig)
    print(f"Dashboard and plots saved in: {PLOTS}")


if __name__ == "__main__":
    create_dashboard()
