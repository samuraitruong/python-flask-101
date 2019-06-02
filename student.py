class Student:
    school_name = "Truong Nguyen Uni"

    def __init__(self, name, student_id: object = 1, student_lastname="") -> object:
        self.name = name;
        self.student_id = student_id;
        self.lastname  = student_lastname;
        # students.append(self)

    def __str__(self):
        return "Student : " + self.name

    def get_uni_name(self):
        return self.school_name;
