import os
import pandas as pd


class Database:

    def __init__(self, file_path="data/students.csv"):
        self.file_path = file_path

        self.columns = [
            "Student_ID",
            "Name",
            "Age",
            "Gender",
            "Study_Hours",
            "Attendance",
            "Previous_Marks",
            "Assignment_Score",
            "Quiz_Score",
            "Final_Marks"
        ]

        self.initialize_database()

    def initialize_database(self):
        folder = os.path.dirname(self.file_path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.file_path, index=False)

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)

            # Ensure all required columns exist
            for column in self.columns:
                if column not in df.columns:
                    df[column] = None

            return df[self.columns]

        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=self.columns)

    def save_data(self, df):
        df.to_csv(self.file_path, index=False)