class Student:
    def __init__(self, name, program, mark):
        self.name = name
        self.program = program
        self.mark = mark


# Creating an empty list
students = []

with open("student_data.txt", "r") as f:
    for line in f:
        name, program, mark = line.strip().split(",")

        s = Student(name, program, int(mark))

        students.append(s)

for student in students:
    print(f"Name: {student.name}")
    print(f"Program: {student.program}")
    print(f"Mark: {student.mark}")
