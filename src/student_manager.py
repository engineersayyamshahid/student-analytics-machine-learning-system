import pandas as pd


class StudentManager:

    def __init__(self, database):
        self.database = database

    def get_number(self, message, data_type=float, minimum=None, maximum=None):
        while True:
            try:
                value = data_type(input(message))

                if minimum is not None and value < minimum:
                    print(f"Value must be at least {minimum}.")
                    continue

                if maximum is not None and value > maximum:
                    print(f"Value must not be greater than {maximum}.")
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def add_student(self):
        df = self.database.load_data()

        print("\n" + "=" * 50)
        print("ADD NEW STUDENT")
        print("=" * 50)

        student_id = self.get_number(
            "Student ID: ",
            int,
            1
        )

        if not df.empty:
            if student_id in df["Student_ID"].astype(int).values:
                print("\nStudent ID already exists.")
                return

        name = input("Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        age = self.get_number(
            "Age: ",
            int,
            1,
            100
        )

        gender = input("Gender: ").strip()

        study_hours = self.get_number(
            "Study Hours Per Day: ",
            float,
            0,
            24
        )

        attendance = self.get_number(
            "Attendance Percentage (0-100): ",
            float,
            0,
            100
        )

        previous_marks = self.get_number(
            "Previous Marks (0-100): ",
            float,
            0,
            100
        )

        assignment_score = self.get_number(
            "Assignment Score (0-100): ",
            float,
            0,
            100
        )

        quiz_score = self.get_number(
            "Quiz Score (0-100): ",
            float,
            0,
            100
        )

        final_marks = self.get_number(
            "Final Marks (0-100): ",
            float,
            0,
            100
        )

        new_student = {
            "Student_ID": student_id,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Study_Hours": study_hours,
            "Attendance": attendance,
            "Previous_Marks": previous_marks,
            "Assignment_Score": assignment_score,
            "Quiz_Score": quiz_score,
            "Final_Marks": final_marks
        }

        new_df = pd.DataFrame([new_student])

        df = pd.concat(
            [df, new_df],
            ignore_index=True
        )

        self.database.save_data(df)

        print(f"\nStudent '{name}' added successfully.")

    def view_all_students(self):
        df = self.database.load_data()

        print("\n" + "=" * 80)
        print("ALL STUDENTS")
        print("=" * 80)

        if df.empty:
            print("No student records found.")
            return

        print(df.to_string(index=False))

    def search_student(self):
        student_id = input(
            "\nEnter Student ID: "
        ).strip()

        if not student_id.isdigit():
            print("Invalid Student ID.")
            return None

        student = self.get_student_by_id(
            int(student_id)
        )

        if student.empty:
            print("Student not found.")
            return None

        print("\n" + "=" * 50)
        print("STUDENT FOUND")
        print("=" * 50)

        print(student.to_string(index=False))

        return student

    def get_student_by_id(self, student_id):
        df = self.database.load_data()

        if df.empty:
            return df

        student = df[
            df["Student_ID"].astype(int) == int(student_id)
        ]

        return student

    def update_student(self):
        df = self.database.load_data()

        if df.empty:
            print("No students available.")
            return

        student_id = input(
            "\nEnter Student ID to update: "
        ).strip()

        if not student_id.isdigit():
            print("Invalid Student ID.")
            return

        student_id = int(student_id)

        matching_indexes = df[
            df["Student_ID"].astype(int) == student_id
        ].index

        if len(matching_indexes) == 0:
            print("Student not found.")
            return

        index = matching_indexes[0]

        print("\nLeave blank to keep the current value.")

        fields = {
            "Name": str,
            "Age": int,
            "Gender": str,
            "Study_Hours": float,
            "Attendance": float,
            "Previous_Marks": float,
            "Assignment_Score": float,
            "Quiz_Score": float,
            "Final_Marks": float
        }

        for field, data_type in fields.items():
            old_value = df.loc[index, field]

            new_value = input(
                f"{field} [{old_value}]: "
            ).strip()

            if new_value == "":
                continue

            try:
                value = data_type(new_value)

                if field == "Attendance":
                    if value < 0 or value > 100:
                        print("Attendance must be between 0 and 100.")
                        continue

                if "Marks" in field or "Score" in field:
                    if value < 0 or value > 100:
                        print("Marks must be between 0 and 100.")
                        continue

                df.loc[index, field] = value

            except ValueError:
                print(f"Invalid value for {field}. Skipped.")

        self.database.save_data(df)

        print("\nStudent updated successfully.")

    def delete_student(self):
        df = self.database.load_data()

        if df.empty:
            print("No students available.")
            return

        student_id = input(
            "\nEnter Student ID to delete: "
        ).strip()

        if not student_id.isdigit():
            print("Invalid Student ID.")
            return

        student_id = int(student_id)

        student = self.get_student_by_id(student_id)

        if student.empty:
            print("Student not found.")
            return

        print("\nStudent Record:")
        print(student.to_string(index=False))

        confirm = input(
            "\nAre you sure you want to delete this student? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            df = df[
                df["Student_ID"].astype(int) != student_id
            ]

            self.database.save_data(df)

            print("Student deleted successfully.")

        else:
            print("Deletion cancelled.")