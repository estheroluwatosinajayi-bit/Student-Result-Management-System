from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
from storage import save_students, load_students

app = Flask(__name__)
app.secret_key = "student-management-secret-key"

students = load_students()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view-students")
def view_students():
    return render_template("view_students.html", students=students)


@app.route("/students", methods=["GET", "POST"])
def student_records():

    if request.method == "POST":

        student_id = request.form["student_id"].strip()
        name = request.form["name"].strip()
        student_class = request.form["student_class"].strip()
        gender = request.form["gender"]
        dob = request.form["dob"]

        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            flash("Please enter a valid date of birth.")
            return redirect("/students")

        if any(s["student_id"] == student_id for s in students):
            flash("This Student ID already exists.")
            return redirect("/students")

        student = {
            "student_id": student_id,
            "name": name,
            "class": student_class,
            "gender": gender,
            "date_of_birth": dob,
            "scores": {}
        }

        students.append(student)
        save_students(students)

        flash("Student registered successfully!")
        return redirect("/students")
@app.route("/results")
def results():
    return render_template("results.html", students=students)
@app.route("/enter-scores", methods=["GET", "POST"])
def enter_scores():

    subjects = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]

    if request.method == "POST":
        student_id = request.form["student_id"]

        student = next(
            (s for s in students if s["student_id"] == student_id),
            None
        )

        if student is None:
            flash("Student not found!")
            return redirect("/enter-scores")

        scores = {}

        try:
            for subject in subjects:
                score = float(request.form[subject])

                if not 0 <= score <= 100:
                    flash("Scores must be between 0 and 100.")
                    return redirect("/enter-scores")

                scores[subject] = score

        except ValueError:
            flash("Please enter valid scores.")
            return redirect("/enter-scores")

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

        student["scores"] = scores
        student["total"] = total
        student["average"] = round(average, 2)
        student["grade"] = grade

        save_students(students)

        flash("Results saved successfully!")
        return redirect("/results")

    return render_template("enter_scores.html", students=students, subjects=subjects)
@app.route("/class-average", methods=["GET", "POST"])
def class_average():

    report = None

    if request.method == "POST":
        class_name = request.form["class_name"].strip().lower()

        class_students = [
            s for s in students
            if s["class"].lower() == class_name and "average" in s
        ]

        if class_students:
            averages = [s["average"] for s in class_students]

            highest = max(class_students, key=lambda s: s["average"])
            lowest = min(class_students, key=lambda s: s["average"])

            report = {
                "class_name": class_name,
                "number": len(class_students),
                "highest": highest,
                "lowest": lowest,
                "average": round(sum(averages) / len(averages), 2)
            }

        else:
            flash("No students with results found in this class.")

    return render_template("class_average.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)