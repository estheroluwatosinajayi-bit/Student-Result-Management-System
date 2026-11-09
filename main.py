from student import register_student, view_students, search_student, update_student, delete_student, restore_student, sort_students, students, deleted_students
from result import enter_scores, view_student_result, generate_class_report
from storage import save_students, load_students, load_deleted_students

students.extend(load_students())
deleted_students.extend(load_deleted_students())

while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Register Student")
    print("2. View Students")
    print("3. Enter Student Scores")
    print("4. view student result")
    print("5. search student")
    print("6. update student")
    print("7. delete student")
    print("8. Restore deleted student")
    print("9. sort students")
    print("10.Generate class report")
    print("11.Exit")

    choice = input("Select an option: ")

    if choice == "1":
        register_student()
        save_students(students)

    elif choice == "2":
        view_students()

    elif choice == "3":
        enter_scores()

    elif choice == "4":
      view_student_result()

    elif choice == "5":
        search_student()

    elif choice == "6":
        update_student()

    elif choice == "7":
        delete_student()

    elif choice == "8":
        restore_student()   

    elif choice == "9":
        sort_students()    


    elif choice == "10":
        generate_class_report()
        
    elif choice == "11":
       save_students(students)
       print("Thank you for using the system!")
       break

    else:
        print("Invalid option. Please try again.")


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