from student import find_student
from storage import save_students
from student import students

def calculate_result(scores):
    total = sum(scores.values())
    average = total / len(scores)

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    return total, average, grade


def enter_scores():
    print("\nENTER STUDENT SCORES")

    student_id = input("Enter Student ID: ")

    student = find_student(student_id)

    if student is None:
        print("Student not found!")
        return

    subjects = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]

    scores = {}

    for subject in subjects:
        while True:
            try:
                score = float(input("Enter score for " + subject + ": "))

                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total, average, grade = calculate_result(scores)

    student["scores"] = scores
    student["total"] = total
    student["average"] = round(average, 2)
    student["grade"] = grade

    save_students(students)

    print("\nRESULT SAVED SUCCESSFULLY!")
    print("Student Name:", student["name"])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("6. Exityh" \
    "")

def view_student_result():
    print("\n===== VIEW STUDENT RESULT =====")

    student_id = input("Enter Student ID: ")

    student = find_student(student_id)

    if student is None:
        print("Student not found!")
        return

    if not student["scores"]:
        print("No scores have been entered for this student.")
        return

    print("\n===== STUDENT REPORT CARD =====")
    print("Student ID:", student["student_id"])
    print("Name:", student["name"])

    for subject, score in student["scores"].items():
        print(subject + ":", score)

    print("----------------------")
    print("Total Score:", student["total"])
    print("Average:", student["average"])
    print("Grade:", student["grade"])    



def generate_class_report():

    print("\n===== CLASS REPORT =====")


    class_name = input("Enter Class/Form: ").lower()

    class_students = []

    for student in students:
        if student["class"].lower() == class_name:
            if "average" in student:
                class_students.append(student)

    if len(class_students) == 0:
        print("No students with results found in this class.")
        return

    averages = [student["average"] for student in class_students]

    highest = max(class_students, key=lambda s: s["average"])
    lowest = min(class_students, key=lambda s: s["average"])

    class_average = sum(averages) / len(averages)





    print("Overall Class Average:", round(class_average, 2))




    print("\n===== CLASS PERFORMANCE =====")
    print("Class:", class_name)
    print("Number of Students:", len(class_students))

    print("\nHighest Average:")
    print(highest["name"], "-", highest["average"])

    print("\nLowest Average:")
    print(lowest["name"], "-", lowest["average"])

    print("\nOverall Class Average:", round(class_average, 2))



    with open("class_report.txt", "w") as file:
        file.write("===== CLASS REPORT =====\n")
        file.write("Class: " + class_name + "\n")
        file.write("Number of Students: " + str(len(class_students)) + "\n")

        file.write("\nHighest Average: " + highest["name"] + " - " + str(highest["average"]) + "\n")
        file.write("Lowest Average: " + lowest["name"] + " - " + str(lowest["average"]) + "\n")
        file.write("Overall Class Average: " + str(round(class_average, 2)) + "\n")

        file.write("\nSTUDENT RESULTS\n")

        for student in class_students:
            file.write(student["name"] + " - " + str(student["average"]) + "\n")

print("Class report saved successfully as class_report.txt")