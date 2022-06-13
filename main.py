# Object Oriented Programming - OOP example in Python


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # grade is a list of grades

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False


if __name__ == '__main__':
    pass


