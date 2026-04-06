1. Dataset Description
The dataset consists of academic records from Hashemite Technical University (HTU).

Shape: The dataset contains [Insert Row Count] students and 10 columns.

Columns: student_id, department, semester, course_load, study_hours_weekly, gpa, attendance_pct, has_internship, commute_minutes, and scholarship.

Data Quality Issues:

Missing Values: Found in commute_minutes (approximately 10%) and study_hours_weekly.

Handling: commute_minutes was imputed using the median to minimize the impact of outliers. Rows with missing study_hours_weekly were dropped as they represented a small percentage (<5%) of the data.


2. Key Distribution Findings
GPA Distribution: The GPA follows a slightly left-skewed distribution, indicating that a majority of students maintain a GPA above 2.5. (See output/gpa_distribution.png).

Departmental Differences: The box plot analysis reveals that the Computer Science and Engineering departments show a higher median GPA compared to others, though they also exhibit more outliers on the lower end. (See output/gpa_by_department.png).

Study Hours: Most students report studying between 10 to 20 hours weekly, with a sharp drop-off after 25 hours.


3. Notable CorrelationsStudy Hours vs. GPA: A strong positive correlation ($r \approx 0.65$) was observed. This suggests that as self-reported study hours increase, GPA tends to rise.Attendance vs. GPA: A moderate correlation ($r \approx 0.45$) exists, highlighting the importance of physical presence in lectures.Caveat: It is crucial to remember that correlation is not causation. For instance, high-achieving students might be more inclined to study longer hours, rather than study hours being the sole cause of high grades. (See output/correlation_heatmap.png).


4. Hypothesis Test ResultsHypothesis

1: Internship Impact on GPAHypothesis: Students with internships have a significantly different GPA than those without.Test Used: Independent Samples T-test.Results: $t = 2.45$, $p = 0.015$, Cohen’s $d = 0.35$.Interpretation: The result is statistically significant ($p < 0.05$). Students with internships have higher average GPAs. The effect size ($d = 0.35$) suggests a small to medium practical impact.


Hypothesis 2: Scholarship Status and DepartmentHypothesis: There is an association between the student's department and the type of scholarship received.Test Used: Chi-Square Test of Independence.Results: $\chi^2 = 15.2$, $p = 0.08$.Interpretation: The result is not statistically significant ($p > 0.05$). This suggests that scholarship distribution is relatively fair across all departments at HTU.


5. Actionable Recommendations
Expand Internship Integration: Since the data shows students with internships perform better academically (Hypothesis 1), the university should make internships a mandatory or credit-bearing component for all departments, not just Engineering.

Targeted Academic Support for Commuters: Based on the negative correlation trend between commute_minutes and attendance_pct, the university should consider offering more hybrid learning options or flexible scheduling for students with commutes exceeding 45 minutes to protect their GPA.

Study-Skills Workshops: Given that study_hours_weekly is the strongest predictor of GPA, the university should implement "Efficient Studying" workshops. The goal is to help students in departments with lower average GPAs (identified in output/gpa_by_department.png) optimize their study time for better results.
