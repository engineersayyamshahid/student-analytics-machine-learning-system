from src.database import Database
from src.student_manager import StudentManager
from src.analytics import Analytics
from src.visualization import Visualization
from src.ml_model import MLModel


def print_menu():

    print("\n")

    print("=" * 70)
    print("STUDENT ANALYTICS & MACHINE LEARNING SYSTEM")
    print("=" * 70)

    print("\nSTUDENT MANAGEMENT")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Individual Student")
    print("4. Update Student")
    print("5. Delete Student")

    print("\nINDIVIDUAL STUDENT ANALYSIS")

    print("6. Individual Statistical Analysis")
    print("7. Individual Probability Analysis")
    print("8. Individual Bayes Analysis")
    print("9. Student vs Class Comparison")
    print("10. ML Performance Prediction")

    print("\nCOMPLETE CLASS ANALYSIS")

    print("11. View Dataset")
    print("12. Complete Class Statistical Analysis")
    print("13. Class Probability Analysis")
    print("14. Class Bayes Analysis")
    print("15. Normal Distribution")
    print("16. Correlation Analysis")
    print("17. Hypothesis Testing")

    print("\nMACHINE LEARNING")

    print("18. Train Linear Regression Model")

    print("\nSYSTEM")

    print("19. Exit")

    print("=" * 70)


def get_student(student_manager):

    student_id = input(
        "\nEnter Student ID: "
    ).strip()

    if not student_id.isdigit():

        print(
            "Invalid Student ID."
        )

        return None

    student = (
        student_manager.get_student_by_id(
            int(student_id)
        )
    )

    if student.empty:

        print(
            "Student not found."
        )

        return None

    return student


def main():

    database = Database()

    student_manager = StudentManager(
        database
    )

    analytics = Analytics(
        database
    )

    visualization = Visualization(
        database
    )

    ml_model = MLModel(
        database
    )

    while True:

        print_menu()

        choice = input(
            "\nEnter your choice (1-19): "
        ).strip()

        if choice == "1":

            student_manager.add_student()

        elif choice == "2":

            student_manager.view_all_students()

        elif choice == "3":

            student_manager.search_student()

        elif choice == "4":

            student_manager.update_student()

        elif choice == "5":

            student_manager.delete_student()

        elif choice == "6":

            student = get_student(
                student_manager
            )

            if student is not None:

                analytics.individual_statistics(
                    student
                )

        elif choice == "7":

            student = get_student(
                student_manager
            )

            if student is not None:

                analytics.individual_probability(
                    student
                )

        elif choice == "8":

            student = get_student(
                student_manager
            )

            if student is not None:

                analytics.individual_bayes(
                    student
                )

        elif choice == "9":

            student = get_student(
                student_manager
            )

            if student is not None:

                visualization.student_vs_class(
                    student
                )

        elif choice == "10":

            student = get_student(
                student_manager
            )

            if student is not None:

                ml_model.predict_student(
                    student
                )

        elif choice == "11":

            student_manager.view_all_students()

        elif choice == "12":

            analytics.class_statistics()

        elif choice == "13":

            analytics.class_probability()

        elif choice == "14":

            analytics.class_bayes()

        elif choice == "15":

            visualization.normal_distribution()

        elif choice == "16":

            visualization.correlation_analysis()

        elif choice == "17":

            analytics.hypothesis_test()

        elif choice == "18":

            ml_model.train_model()

        elif choice == "19":

            print(
                "\nThank you for using the "
                "Student Analytics System."
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1 to 19."
            )


if __name__ == "__main__":
    main()