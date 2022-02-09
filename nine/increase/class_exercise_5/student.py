# Write a python class named student with two attributes student_name, marks.
# Modify the attribute values of the said class and print the original and modified values of the said attributes.





class Student:
    def __init__(self):
        self.student_name = "student_name"
        self.marks = 0

    def set_student_name(self, student_name):
        self.student_name = student_name

    def set_marks(self, marks):
        self.marks = marks

names = Student()
# print(names)

names.set_student_name("Sho")
print(names.student_name)

names.set_marks(1234)
print(names.marks)

        