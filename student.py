from storage import save_students, save_deleted_students
from datetime import datetime
students = []
deleted_students = []

class Student:
    def __init__(self, student_id, name, student_class, gender, dob):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Class:", self.student_class)
        print("Gender:", self.gender)
        print("Date of Birth:", self.dob)

def register_student():
    print("\nSTUDENT REGISTRATION")

    student_id = input("Enter Student ID: ")
    name = input("Enter Full Name: ")
    student_class = input("Enter Class: ")
    gender = input("Enter Gender: ")
    while True:
        try:
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            datetime.strptime(dob, "%Y-%m-%d")
            break
        except ValueError:
          print("Invalid date! Please use YYYY-MM-DD.")

    student_record = Student(student_id, name, student_class, gender, dob)

    student = {
    "student_id": student_record.student_id,
    "name": student_record.name,
    "class": student_record.student_class,
    "gender": student_record.gender,
    "date_of_birth": student_record.dob,
    "scores": {}
}
    students.append(student)

    print("\nStudent registered successfully!")


def view_students():
    print("\nREGISTERED STUDENTS")

    if len(students) == 0:
        print("No students registered yet.")

    else:
        for student in students:
            print("----------------------")
            print("Student ID:", student["student_id"])
            print("Name:", student["name"])
            print("Class:", student["class"])
            print("Gender:", student["gender"])
            print("Date of Birth:", student["date_of_birth"])
            print("----------------------")


def find_student(student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student

    return None



def search_student():
    print("\n===== SEARCH STUDENT =====")

    search = input("Enter Student ID or Name: ").lower()

    found = False

    for student in students:
        if (search == student["student_id"].lower()
                or search in student["name"].lower()):

            print("\nStudent Found!")
            print("Student ID:", student["student_id"])
            print("Name:", student["name"])
            print("Class:", student["class"])
            print("Gender:", student["gender"])
            print("Date of Birth:", student["date_of_birth"])

            found = True

    if not found:
        print("Student not found!")


def update_student():
    print("\n===== UPDATE STUDENT DETAILS =====")

    student_id = input("Enter Student ID: ")

    student = find_student(student_id)

    if student is None:
        print("Student not found!")
        return

    print("Leave a field empty if you don't want to change it.")

    name = input("Enter new Full Name: ")
    student_class = input("Enter new Class: ")
    gender = input("Enter new Gender: ")
    dob = input("Enter new Date of Birth: ")

    if name:
        student["name"] = name

    if student_class:
        student["class"] = student_class

    if gender:
        student["gender"] = gender

    if dob:
        student["date_of_birth"] = dob

    save_students(students)

    print("Student details updated successfully!")



def delete_student():
    print("\n===== DELETE STUDENT =====")

    student_id = input("Enter Student ID: ")

    student = find_student(student_id)

    if student is None:
        print("Student not found!")
        return

    confirm = input("Are you sure you want to delete this student? (yes/no): ").lower()

    if confirm == "yes":
      students.remove(student)
      deleted_students.append(student)

      save_students(students)
      save_deleted_students(deleted_students)

      print("Student deleted successfully!")
      print("You can restore this student later.")

def restore_student():
    print("\n===== RESTORE DELETED STUDENT =====")

    student_id = input("Enter Student ID to restore: ")

    student = None

    for record in deleted_students:
        if record["student_id"] == student_id:
            student = record
            break

    if student is None:
        print("Deleted student not found!")
        return

    if find_student(student_id) is not None:
        print("This student is already registered!")
        return

    deleted_students.remove(student)
    students.append(student)

    save_students(students)
    save_deleted_students(deleted_students)

    print("Student restored successfully!")  


def sort_students():
    print("\n===== SORT STUDENTS =====")
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Average (Highest to Lowest)")

    choice = input("Select sorting option: ")

    if choice == "1":
        sorted_students = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda student: student.get("average", 0),
            reverse=True
        )

    else:
        print("Invalid sorting option!")
        return

    print("\n===== SORTED STUDENTS =====")

    for student in sorted_students:
        print("----------------------")
        print("Student ID:", student["student_id"])
        print("Name:", student["name"])
        print("Average:", student.get("average", "No result yet"))    