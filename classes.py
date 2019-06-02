students = []


class Student:
    school_name = "truong uni"

    def __init__(self, name, studen_id: object = 1) -> object:
        self.name = name;
        self.student_id = studen_id;
        students.append(self)

    def __str__(self):
        return "Student : " + self.name

    def get_name(self):
        return self.school_name;


class HighSchoolStudent(Student):

    school_name: "super uni"

    def get_name(self):
        return "high schoo:" + super().get_name()
