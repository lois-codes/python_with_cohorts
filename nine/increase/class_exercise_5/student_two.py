# Write a python class named Student with two attributes student_id, student_name. 
# Add a new attribute student_class and display the entire attribute and their values of the said class.
# Now remove the student_name attribute and display the entire attribute with values.

class Student:
    def __init__(self):
        self.student_id = 0
        self.student_name = "student_name"
        self.student_class = 0


    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_student_name(self, student_name):
        self.student_name = student_name

    def set_student_class(self, student_class):
        self.student_class = student_class
    
identity = Student()

identity.set_student_id(10)
print(identity.student_id)

identity.set_student_name("Kola")
print(identity.student_name)

identity.set_student_class("Cohort 9")
print(identity.student_class)
    