from scipy.stats import percentileofscore
from scipy.stats import ttest_ind


class Analytics:

    def __init__(self, database):
        self.database = database

    def performance_level(self, marks):

        if marks >= 90:
            return "Excellent"

        elif marks >= 80:
            return "Very Good"

        elif marks >= 70:
            return "Good"

        elif marks >= 60:
            return "Average"

        else:
            return "Needs Improvement"

    def individual_statistics(self, student):
        df = self.database.load_data()

        if student.empty or df.empty:
            print("No data available.")
            return

        student_data = student.iloc[0]

        marks = float(
            student_data["Final_Marks"]
        )

        class_marks = df["Final_Marks"]

        class_mean = class_marks.mean()
        class_median = class_marks.median()
        class_variance = class_marks.var()
        class_std = class_marks.std()

        rank_series = class_marks.rank(
            ascending=False,
            method="min"
        )

        student_index = student.index[0]

        rank = rank_series.loc[student_index]

        percentile = percentileofscore(
            class_marks,
            marks,
            kind="rank"
        )

        if class_std != 0:
            z_score = (
                marks - class_mean
            ) / class_std
        else:
            z_score = 0

        difference = marks - class_mean

        print("\n" + "=" * 60)
        print("INDIVIDUAL STUDENT STATISTICAL ANALYSIS")
        print("=" * 60)

        print(f"Student ID: {student_data['Student_ID']}")
        print(f"Name: {student_data['Name']}")
        print(f"Age: {student_data['Age']}")
        print(f"Gender: {student_data['Gender']}")

        print("\nSTUDENT PERFORMANCE")

        print(f"Final Marks: {marks:.2f}")

        print(
            f"Performance Level: "
            f"{self.performance_level(marks)}"
        )

        print(f"Class Rank: {int(rank)}")
        print(f"Percentile: {percentile:.2f}%")

        print("\nCLASS STATISTICAL COMPARISON")

        print(f"Class Mean: {class_mean:.2f}")
        print(f"Class Median: {class_median:.2f}")
        print(f"Class Variance: {class_variance:.2f}")
        print(f"Class Standard Deviation: {class_std:.2f}")

        print("\nSTUDENT POSITION")

        print(f"Z-Score: {z_score:.2f}")

        print(
            f"Difference From Class Mean: "
            f"{difference:.2f}"
        )

    def class_statistics(self):
        df = self.database.load_data()

        if df.empty:
            print("No student data available.")
            return

        marks = df["Final_Marks"]

        print("\n" + "=" * 60)
        print("COMPLETE CLASS STATISTICAL ANALYSIS")
        print("=" * 60)

        print(f"Total Students: {len(df)}")

        print(f"Mean: {marks.mean():.2f}")
        print(f"Median: {marks.median():.2f}")

        mode_values = marks.mode().tolist()

        print(f"Mode: {mode_values}")

        print(f"Variance: {marks.var():.2f}")

        print(
            f"Standard Deviation: "
            f"{marks.std():.2f}"
        )

        print(f"Minimum Marks: {marks.min():.2f}")
        print(f"Maximum Marks: {marks.max():.2f}")

        pass_students = len(
            df[df["Final_Marks"] >= 50]
        )

        fail_students = len(
            df[df["Final_Marks"] < 50]
        )

        pass_percentage = (
            pass_students / len(df)
        ) * 100

        fail_percentage = (
            fail_students / len(df)
        ) * 100

        print("\nCLASS PERFORMANCE")

        print(
            f"Pass Percentage: "
            f"{pass_percentage:.2f}%"
        )

        print(
            f"Fail Percentage: "
            f"{fail_percentage:.2f}%"
        )

    def individual_probability(self, student):
        df = self.database.load_data()

        if student.empty or df.empty:
            print("No data available.")
            return

        student_data = student.iloc[0]

        marks = float(
            student_data["Final_Marks"]
        )

        total_students = len(df)

        pass_probability = (
            len(
                df[df["Final_Marks"] >= 50]
            )
            / total_students
        )

        score_probability = (
            len(
                df[df["Final_Marks"] >= marks]
            )
            / total_students
        )

        class_mean = (
            df["Final_Marks"].mean()
        )

        if marks > class_mean:
            position = "Above Class Average"
        elif marks < class_mean:
            position = "Below Class Average"
        else:
            position = "Equal to Class Average"

        print("\n" + "=" * 60)
        print("INDIVIDUAL STUDENT PROBABILITY ANALYSIS")
        print("=" * 60)

        print(
            f"Student: "
            f"{student_data['Name']}"
        )

        print(
            f"Student Marks: "
            f"{marks:.2f}"
        )

        print(
            f"\nP(Student Passes): "
            f"{pass_probability:.2f}"
        )

        print(
            f"P(Class Students Scoring "
            f"{marks:.2f} or More): "
            f"{score_probability:.2f}"
        )

        print(
            f"\nStudent Position: {position}"
        )

    def class_probability(self):
        df = self.database.load_data()

        if df.empty:
            print("No student data available.")
            return

        total = len(df)

        passing = len(
            df[df["Final_Marks"] >= 50]
        )

        failing = len(
            df[df["Final_Marks"] < 50]
        )

        above_70 = len(
            df[df["Final_Marks"] >= 70]
        )

        above_80 = len(
            df[df["Final_Marks"] >= 80]
        )

        above_90 = len(
            df[df["Final_Marks"] >= 90]
        )

        print("\n" + "=" * 60)
        print("CLASS PROBABILITY ANALYSIS")
        print("=" * 60)

        print(
            f"P(Pass): "
            f"{passing / total:.2f}"
        )

        print(
            f"P(Fail): "
            f"{failing / total:.2f}"
        )

        print(
            f"P(Marks >= 70): "
            f"{above_70 / total:.2f}"
        )

        print(
            f"P(Marks >= 80): "
            f"{above_80 / total:.2f}"
        )

        print(
            f"P(Marks >= 90): "
            f"{above_90 / total:.2f}"
        )

    def individual_bayes(self, student):
        df = self.database.load_data()

        if student.empty or df.empty:
            print("No data available.")
            return

        student_data = student.iloc[0]

        study_hours = float(
            student_data["Study_Hours"]
        )

        if study_hours >= 5:

            condition = (
                df["Study_Hours"] >= 5
            )

            condition_name = (
                "Study Hours >= 5"
            )

        else:

            condition = (
                df["Study_Hours"] < 5
            )

            condition_name = (
                "Study Hours < 5"
            )

        high_performance = (
            df["Final_Marks"] >= 80
        )

        condition_count = len(
            df[condition]
        )

        both_count = len(
            df[
                condition &
                high_performance
            ]
        )

        if condition_count == 0:
            probability = 0
        else:
            probability = (
                both_count /
                condition_count
            )

        print("\n" + "=" * 60)
        print("INDIVIDUAL BAYES / CONDITIONAL PROBABILITY")
        print("=" * 60)

        print(
            f"Student: "
            f"{student_data['Name']}"
        )

        print(
            f"Student Study Hours: "
            f"{study_hours}"
        )

        print(
            "\nConditional Probability:"
        )

        print(
            f"P(High Performance | "
            f"{condition_name})"
        )

        print(
            f"\nProbability: "
            f"{probability:.2f}"
        )

    def class_bayes(self):
        df = self.database.load_data()

        if df.empty:
            print("No data available.")
            return

        study_more = (
            df["Study_Hours"] >= 5
        )

        high_performance = (
            df["Final_Marks"] >= 80
        )

        study_more_count = len(
            df[study_more]
        )

        high_count = len(
            df[high_performance]
        )

        both_count = len(
            df[
                study_more &
                high_performance
            ]
        )

        total = len(df)

        if study_more_count > 0:
            conditional_probability = (
                both_count /
                study_more_count
            )
        else:
            conditional_probability = 0

        prior_high = high_count / total

        prior_study_more = (
            study_more_count / total
        )

        print("\n" + "=" * 60)
        print("CLASS BAYES ANALYSIS")
        print("=" * 60)

        print(
            "High Performance = Final Marks >= 80"
        )

        print(
            "Condition = Study Hours >= 5"
        )

        print(
            f"\nP(High Performance): "
            f"{prior_high:.2f}"
        )

        print(
            f"P(Study Hours >= 5): "
            f"{prior_study_more:.2f}"
        )

        print(
            "\nConditional Probability:"
        )

        print(
            "P(High Performance | Study Hours >= 5)"
        )

        print(
            f"\nResult: "
            f"{conditional_probability:.2f}"
        )

    def hypothesis_test(self):
        df = self.database.load_data()

        if len(df) < 4:
            print(
                "At least 4 students are required "
                "for hypothesis testing."
            )
            return

        group_a = df[
            df["Study_Hours"] < 5
        ]["Final_Marks"]

        group_b = df[
            df["Study_Hours"] >= 5
        ]["Final_Marks"]

        if len(group_a) < 2 or len(group_b) < 2:
            print(
                "Each group requires at least "
                "2 students."
            )
            return

        t_statistic, p_value = ttest_ind(
            group_a,
            group_b,
            equal_var=False
        )

        alpha = 0.05

        print("\n" + "=" * 60)
        print("HYPOTHESIS TESTING")
        print("=" * 60)

        print(
            "H0: Students studying less than 5 hours "
            "and students studying 5 or more hours "
            "have the same average marks."
        )

        print(
            "\nH1: There is a significant difference "
            "between the groups."
        )

        print(
            f"\nT-Statistic: "
            f"{t_statistic:.4f}"
        )

        print(
            f"P-Value: "
            f"{p_value:.4f}"
        )

        print(
            f"Significance Level: "
            f"{alpha}"
        )

        if p_value < alpha:

            print(
                "\nDecision: Reject H0"
            )

            print(
                "Conclusion: The difference between "
                "the two groups is statistically "
                "significant."
            )

        else:

            print(
                "\nDecision: Fail to Reject H0"
            )

            print(
                "Conclusion: There is not enough "
                "statistical evidence to conclude "
                "a significant difference."
            )