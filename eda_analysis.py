"""Lab 4 — Descriptive Analytics: Student Performance EDA

Conduct exploratory data analysis on the student performance dataset.
Produce distribution plots, correlation analysis, hypothesis tests,
and a written findings report.

Usage:
    python eda_analysis.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def load_and_profile(filepath):
    """Load the dataset and generate a data profile report.

    Args:
        filepath: path to the CSV file (e.g., 'data/student_performance.csv')

    Returns:
        DataFrame: the loaded dataset

    Side effects:
        Saves a text profile to output/data_profile.txt containing:
        - Shape (rows, columns)
        - Data types for each column
        - Missing value counts per column
        - Descriptive statistics for numeric columns
    """
    # TODO: Load the dataset and report its shape, data types, missing values,
    #       and descriptive statistics to output/data_profile.txt
    
    df = pd.read_csv(filepath)

    
    os.makedirs("output", exist_ok=True)
    
    with open('output/data_profile.txt', 'w') as f:
        f.write("=== Data Profile Report ===\n\n")
        f.write(f"Shape (rows, columns): {df.shape}\n\n")
        
        f.write("=== Data Types ===\n")
        f.write(f"{df.dtypes}\n\n")
        
        f.write("=== Missing Values ===\n")
        missing = df.isnull().sum()
        percent = (df.isnull().sum() / len(df)) * 100
        f.write(f"{pd.concat([missing, percent], axis=1, keys=['Count', 'Percentage'])}\n\n")
        
        f.write("=== Descriptive Statistics ===\n")
        f.write(f"{df.describe()}\n")

    if 'commute_minutes' in df.columns:
        df['commute_minutes'] = df['commute_minutes'].fillna(df['commute_minutes'].median())
    
    df = df.dropna(subset=['study_hours_weekly'])
    
    return df


def plot_distributions(df):
    """Create distribution plots for key numeric variables.

    Args:
        df: pandas DataFrame with the student performance data

    Returns:
        None

    Side effects:
        Saves at least 3 distribution plots (histograms with KDE or box plots)
        as PNG files in the output/ directory. Each plot should have a
        descriptive title that states what the distribution reveals.
    """
    # TODO: Create distribution plots for numeric columns like GPA,
    #       study hours, attendance, and commute minutes
    # TODO: Use histograms with KDE overlay (sns.histplot) or box plots
    # TODO: Save each plot to the output/ directory
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['gpa'], kde=True, color='skyblue')
    plt.title('Distribution of Student GPA (KDE Overlay)')
    plt.xlabel('GPA')
    plt.savefig('output/gpa_distribution.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='department', y='gpa', data=df, palette='Set3')
    plt.title('GPA Distribution across Departments')
    plt.xticks(rotation=45)
    plt.savefig('output/gpa_by_department.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.histplot(df['study_hours_weekly'], kde=True, color='salmon')
    plt.title('Weekly Study Hours Distribution')
    plt.savefig('output/study_hours_distribution.png')
    plt.close()


def plot_correlations(df):
    """Analyze and visualize relationships between numeric variables.

    Args:
        df: pandas DataFrame with the student performance data

    Returns:
        None

    Side effects:
        Saves at least one correlation visualization to the output/ directory
        (e.g., a heatmap, scatter plot, or pair plot).
    """
    # TODO: Compute the correlation matrix for numeric columns
    # TODO: Create a heatmap or scatter plots showing key relationships
    # TODO: Save the visualization(s) to the output/ directory
    
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap of Student Metrics')
    plt.savefig('output/correlation_heatmap.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='study_hours_weekly', y='gpa', data=df, alpha=0.6)
    plt.title('Relationship: Study Hours vs GPA')
    plt.savefig('output/scatter_study_gpa.png')
    plt.close()


def run_hypothesis_tests(df):
    """Run statistical tests to validate observed patterns.

    Args:
        df: pandas DataFrame with the student performance data

    Returns:
        dict: test results with keys like 'internship_ttest', 'dept_anova',
              each containing the test statistic and p-value

    Side effects:
        Prints test results to stdout with interpretation.

    Tests to consider:
        - t-test: Does GPA differ between students with and without internships?
        - ANOVA: Does GPA differ across departments?
        - Correlation test: Is the correlation between study hours and GPA significant?
    """
    # TODO: Run at least two hypothesis tests on patterns you observe in the data
    # TODO: Report the test statistic, p-value, and your interpretation
    
    results = {}
    print("\n" + "="*30)
    print("HYPOTHESIS TESTING RESULTS")
    print("="*30)

    if 'has_internship' in df.columns:
        group_yes = df[df['has_internship'] == 'Yes']['gpa']
        group_no = df[df['has_internship'] == 'No']['gpa']
        
        t_stat, p_val = stats.ttest_ind(group_yes, group_no, nan_policy='omit')
        results['internship_ttest'] = {'t_stat': t_stat, 'p_value': p_val}
        
        print(f"\n1. Hypothesis: Internships vs GPA")
        print(f"   t-statistic: {t_stat:.4f}, p-value: {p_val:.4f}")
        interpretation = "Significant" if p_val < 0.05 else "Not Significant"
        print(f"   Interpretation: {interpretation} difference in GPA.")

    if 'department' in df.columns:
        depts = df['department'].unique()
        groups = [df[df['department'] == d]['gpa'] for d in depts]
        
        f_stat, p_val_anova = stats.f_oneway(*groups)
        results['dept_anova'] = {'f_stat': f_stat, 'p_value': p_val_anova}
        
        print(f"\n2. Hypothesis: GPA difference across Departments")
        print(f"   F-statistic: {f_stat:.4f}, p-value: {p_val_anova:.4f}")
        interpretation = "Significant" if p_val_anova < 0.05 else "Not Significant"
        print(f"   Interpretation: {interpretation} variation between departments.")

    return results


def main():
    """Orchestrate the full EDA pipeline."""
    
    os.makedirs("output", exist_ok=True)
    
    dataset_path = 'data/student_performance.csv'
    
    if not os.path.exists(dataset_path):
        print(f"Error: {dataset_path} not found.")
        return
    
    
    df = load_and_profile(dataset_path)
    
    plot_distributions(df)

    plot_correlations(df)

    run_hypothesis_tests(df)

    print("\nEDA completed! Check 'output/' directory for files.")
    
    
    # TODO: Load and profile the dataset
    # TODO: Generate distribution plots
    # TODO: Analyze correlations
    # TODO: Run hypothesis tests
    # TODO: Write a FINDINGS.md summarizing your analysis


if __name__ == "__main__":
    main()
