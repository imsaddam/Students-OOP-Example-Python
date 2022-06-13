# Object Oriented Programming - OOP example in Python


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # grade is a list of grades

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

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


student1 = Student('John', 20, 98)
student2 = Student('Jane', 21, 97)
student3 = Student('Jack', 22, 96)

course1 = Course('Python', 2)
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
print(course1.get_average_grade())

