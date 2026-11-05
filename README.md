# Week 4: Data Visualization with Matplotlib and Seaborn

## Project Overview
This project uses Matplotlib and Seaborn to explore a sample student-performance dataset. It creates histograms, scatter plots, a correlation heatmap, a pairplot-style grid, and a combined dashboard.

## Files
- `main.py` — Runs the dashboard project.
- `dashboard.py` — Loads the dataset and creates all visualizations.
- `student_performance.csv` — Sample dataset for analysis.
- `requirements.txt` — Python package requirements.
- `plots/` — Generated plot images and the combined dashboard.

## Concepts Learned
1. **Matplotlib:** Python plotting library used to create and customize charts.
2. **Histogram:** Displays the distribution of a numerical feature such as final scores.
3. **Scatter plot:** Displays the relationship between two numerical features.
4. **Seaborn:** Statistical visualization library built on Matplotlib.
5. **Heatmap:** Represents a matrix of values using visual shading; here it shows feature correlations.
6. **Pairplot:** Displays pairwise relationships and individual distributions for numerical features.
7. **Dashboard:** Combines multiple charts in one view for easier dataset analysis.

## Hands-On Activities
- Plot a histogram of final scores.
- Compare study hours with final scores using a scatter plot.
- Visualize numerical feature correlations with a heatmap.
- Explore pairwise relationships using a pairplot-style grid.
- Combine selected charts into a 2x2 dashboard.

## Client Project: Student Performance Dashboard
The sample dataset includes hours studied, attendance, previous score, and final score. The dashboard helps explore relationships among these features. It saves each chart and a combined dashboard image in the `plots` folder.

**Dataset note:** The data is illustrative sample data created for this learning exercise, not real student or institutional data. A visible relationship does not by itself prove causation.

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Install packages: `pip install -r requirements.txt`
4. Run: `python main.py`

The generated images are saved in `plots/`.

## Output Images
- `histogram_final_scores.png`
- `scatter_study_hours_vs_score.png`
- `correlation_heatmap.png`
- `pairplot_student_performance.png`
- `student_performance_dashboard.png`
