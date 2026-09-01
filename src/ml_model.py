import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class MLModel:

    def __init__(self, database):
        self.database = database

        self.features = [
            "Study_Hours",
            "Attendance",
            "Previous_Marks",
            "Assignment_Score",
            "Quiz_Score"
        ]

        os.makedirs(
            "models",
            exist_ok=True
        )

        self.model_path = (
            "models/"
            "student_performance_model.pkl"
        )

    def train_model(self):
        df = self.database.load_data()

        if len(df) < 6:
            print(
                "At least 6 students are required "
                "to train the ML model."
            )
            return None

        X = df[self.features]

        y = df["Final_Marks"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.25,
            random_state=42
        )

        model = LinearRegression()

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        mse = mean_squared_error(
            y_test,
            predictions
        )

        r2 = r2_score(
            y_test,
            predictions
        )

        print("\n" + "=" * 60)
        print("LINEAR REGRESSION MODEL PERFORMANCE")
        print("=" * 60)

        print(
            f"Mean Absolute Error: "
            f"{mae:.2f}"
        )

        print(
            f"Mean Squared Error: "
            f"{mse:.2f}"
        )

        print(
            f"R² Score: "
            f"{r2:.2f}"
        )

        print("\nFeatures Used:")

        for feature in self.features:
            print(f"- {feature}")

        joblib.dump(
            model,
            self.model_path
        )

        print(
            "\nModel trained and saved successfully."
        )

        return model

    def load_or_train_model(self):
        if os.path.exists(
            self.model_path
        ):

            try:
                return joblib.load(
                    self.model_path
                )

            except Exception:
                return self.train_model()

        return self.train_model()

    def predict_student(self, student):
        if student.empty:
            print("Student not found.")
            return

        model = self.load_or_train_model()

        if model is None:
            return

        student_data = student.iloc[0]

        input_data = pd.DataFrame(
            [[
                student_data["Study_Hours"],
                student_data["Attendance"],
                student_data["Previous_Marks"],
                student_data["Assignment_Score"],
                student_data["Quiz_Score"]
            ]],
            columns=self.features
        )

        prediction = model.predict(
            input_data
        )[0]

        actual_marks = float(
            student_data["Final_Marks"]
        )

        difference = (
            actual_marks -
            prediction
        )

        print("\n" + "=" * 60)
        print("INDIVIDUAL ML PERFORMANCE PREDICTION")
        print("=" * 60)

        print(
            f"Student: "
            f"{student_data['Name']}"
        )

        print(
            f"Actual Final Marks: "
            f"{actual_marks:.2f}"
        )

        print(
            f"Predicted Final Marks: "
            f"{prediction:.2f}"
        )

        print(
            f"Actual - Predicted Difference: "
            f"{difference:.2f}"
        )

        if prediction >= 90:
            level = "Excellent"

        elif prediction >= 80:
            level = "Very Good"

        elif prediction >= 70:
            level = "Good"

        elif prediction >= 60:
            level = "Average"

        else:
            level = "Needs Improvement"

        print(
            f"Predicted Performance Level: "
            f"{level}"
        )