from flask import Flask, render_template, redirect, url_for, request
from student import Student

app = Flask(__name__)

students = []


@app.route('/', methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        student_name = request.form.get("name", "")
        student_lastname = request.form.get("student_lastname", "")
        student_id = request.form.get("student_id", "")
        delete_student_id = request.form.get("delete_student_id", "")
        if delete_student_id != "":
            print("delete students" + delete_student_id)
            toberemove = 0;
            for x in students:
                if (x.student_id == delete_student_id):
                    toberemove = x

            students.remove(toberemove)

        else:
            print("student_name=" + student_name);
            new_student = Student(name=student_name, student_id=student_id, student_lastname=student_lastname)
            students.append(new_student)
        return redirect(url_for("students_page"))

    return render_template('index.html', students=students)


if __name__ == "__main__":
    app.run(debug=True)
