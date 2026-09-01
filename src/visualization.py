import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import norm


class Visualization:

    def __init__(self, database):
        self.database = database

        os.makedirs(
            "visualizations",
            exist_ok=True
        )

    def normal_distribution(self):
        df = self.database.load_data()

        if len(df) < 2:
            print(
                "At least 2 students are required."
            )
            return

        marks = df["Final_Marks"]

        mean = marks.mean()
        std = marks.std()

        print("\n" + "=" * 60)
        print("NORMAL DISTRIBUTION ANALYSIS")
        print("=" * 60)

        print(f"Mean: {mean:.2f}")
        print(
            f"Standard Deviation: "
            f"{std:.2f}"
        )

        plt.figure(figsize=(10, 6))

        sns.histplot(
            marks,
            bins=min(10, len(marks)),
            stat="density",
            kde=True
        )

        if std > 0:

            x = np.linspace(
                marks.min() - 5,
                marks.max() + 5,
                200
            )

            y = norm.pdf(
                x,
                mean,
                std
            )

            plt.plot(
                x,
                y,
                linewidth=2
            )

        plt.title(
            "Student Final Marks Normal Distribution"
        )

        plt.xlabel(
            "Final Marks"
        )

        plt.ylabel(
            "Density"
        )

        plt.grid(True)

        file_path = (
            "visualizations/"
            "normal_distribution.png"
        )

        plt.savefig(
            file_path,
            bbox_inches="tight"
        )

        plt.show()

        print(
            f"\nGraph saved to: {file_path}"
        )

    def correlation_analysis(self):
        df = self.database.load_data()

        if len(df) < 2:
            print(
                "At least 2 students are required."
            )
            return

        numerical_columns = [
            "Study_Hours",
            "Attendance",
            "Previous_Marks",
            "Assignment_Score",
            "Quiz_Score",
            "Final_Marks"
        ]

        correlation = df[
            numerical_columns
        ].corr()

        print("\n" + "=" * 60)
        print("CORRELATION ANALYSIS")
        print("=" * 60)

        print("\nCorrelation with Final Marks:\n")

        final_correlation = correlation[
            "Final_Marks"
        ].sort_values(
            ascending=False
        )

        print(final_correlation)

        print(
            "\nComplete Correlation Matrix:\n"
        )

        print(correlation)

        plt.figure(figsize=(11, 8))

        sns.heatmap(
            correlation,
            annot=True,
            fmt=".2f",
            cmap="coolwarm"
        )

        plt.title(
            "Student Performance Correlation Heatmap"
        )

        file_path = (
            "visualizations/"
            "correlation_heatmap.png"
        )

        plt.savefig(
            file_path,
            bbox_inches="tight"
        )

        plt.show()

        print(
            f"\nGraph saved to: {file_path}"
        )

    def student_vs_class(self, student):
        df = self.database.load_data()

        if student.empty or df.empty:
            print("No data available.")
            return

        student_data = student.iloc[0]

        student_name = (
            student_data["Name"]
        )

        student_marks = float(
            student_data["Final_Marks"]
        )

        class_average = (
            df["Final_Marks"].mean()
        )

        print("\n" + "=" * 60)
        print("STUDENT VS CLASS COMPARISON")
        print("=" * 60)

        print(
            f"Student: "
            f"{student_name}"
        )

        print(
            f"Student Marks: "
            f"{student_marks:.2f}"
        )

        print(
            f"Class Average: "
            f"{class_average:.2f}"
        )

        difference = (
            student_marks -
            class_average
        )

        print(
            f"Difference: "
            f"{difference:.2f}"
        )

        plt.figure(figsize=(8, 5))

        labels = [
            student_name,
            "Class Average"
        ]

        values = [
            student_marks,
            class_average
        ]

        plt.bar(
            labels,
            values
        )

        plt.ylim(0, 100)

        plt.ylabel("Marks")

        plt.title(
            f"{student_name} vs Class Average"
        )

        file_name = (
            student_name
            .replace(" ", "_")
            .lower()
        )

        file_path = (
            f"visualizations/"
            f"{file_name}_vs_class.png"
        )

        plt.savefig(
            file_path,
            bbox_inches="tight"
        )

        plt.show()

        print(
            f"\nGraph saved to: {file_path}"
        )