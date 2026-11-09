import json
import os
def save_students(students):
    os.makedirs("data", exist_ok=True)

    try:
        with open("data/students.json", "w") as file:
            json.dump(students, file, indent=4)

    except Exception as error:
        print("Error saving records:", error)

    else:
        print("Student records saved successfully!")

    finally:
        print("Save operation completed.")


def load_students():
    try:
        with open("data/students.json", "r") as file:
            students = json.load(file)

        return students

    except FileNotFoundError:
        print("No previous student records found.")
        return []

    except json.JSONDecodeError:
        print("The student data file is empty or invalid.")
        return []



def save_deleted_students(deleted_students):
    os.makedirs("data", exist_ok=True)

    try:
        with open("data/deleted_students.json", "w") as file:
            json.dump(deleted_students, file, indent=4)

        print("Deleted student records saved!")

    except Exception as error:
        print("Error saving deleted records:", error)


def load_deleted_students():
    try:
        with open("data/deleted_students.json", "r") as file:
            deleted_students = json.load(file)

        return deleted_students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Deleted student data file is invalid.")
        return []