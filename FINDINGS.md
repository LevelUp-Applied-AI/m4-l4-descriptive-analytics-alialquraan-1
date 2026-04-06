## 1. Dataset Description
The dataset consists of academic records from Hashemite Technical University (HTU).
* **Shape:** The dataset contains **2000 students** and 10 columns.
* **Data Types:** A mix of categorical (str) and numerical (float64/int64) data.
* **Data Quality Issues:** * **commute_minutes:** Missing in 181 rows (9.05%). These were imputed with the median (25.0 minutes).
    * **scholarship:** Missing in 389 rows (19.45%). These represent students with "None" or unspecified status.
    * **study_hours_weekly:** Cleaned to ensure no null values remained in the analysis.

## 2. Key Distribution Findings
* **GPA Distribution:** The mean GPA is **2.77**, with a minimum of 1.31 and a maximum of 4.0. The distribution is relatively normal but slightly centered around the 2.78 median. (See `output/gpa_distribution.png`).
* **Departmental Differences:** The box plot analysis reveals that GPA is consistently distributed across departments with no extreme variations in the median. (See `output/gpa_by_department.png`).
* **Commute Time:** The average student commutes for about **25.5 minutes**, but some students face commutes up to 79 minutes.

## 3. Notable Correlations
* **Study Hours vs. GPA:** A clear positive trend exists. The average student studies **14.88 hours** per week.
* **Attendance:** The average attendance rate is **77.4%**, which shows a moderate positive relationship with academic success. (See `output/correlation_heatmap.png`).
* **Caveat:** Correlation does not imply causation; while high study hours correlate with high GPAs, other factors like prior knowledge may also contribute.

## 4. Hypothesis Test Results

### Hypothesis 1: Internship Impact on GPA
* **Hypothesis:** Students with internships have a significantly different GPA than those without.
* **Test Used:** Independent Samples T-test.
* **Results:** **t = 13.5644, p = 0.0000**.
* **Interpretation:** **Statistically Significant.** Students with internships perform significantly better academically. The zero p-value indicates that this result is highly reliable and not due to random chance.

### Hypothesis 2: GPA Variation Across Departments
* **Hypothesis:** Does GPA differ significantly across the various university departments?
* **Test Used:** ANOVA (One-way).
* **Results:** **F = 0.6671, p = 0.6148**.
* **Interpretation:** **Not Significant.** Since the p-value (0.61) is much higher than 0.05, we conclude that there is no meaningful difference in GPA between departments.

## 5. Actionable Recommendations
1. **Mandatory Internship Credits:** Given the high t-statistic (13.56) for internships, the university should integrate mandatory internships to boost overall student GPA.
2. **Attendance Intervention:** With an average attendance of 77%, the university should implement an early warning system for students dropping below 70% to prevent GPA decline.
3. **Commuter Support:** Since nearly 10% of data was missing for commute times and some students travel up to 79 minutes, offering hybrid lectures could help those with long commutes maintain their performance.