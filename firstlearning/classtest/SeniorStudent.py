# sub class inherit from student
from Student import Student

class SeniorStudent(Student):
    """sub class inherit from student"""

    def __init__(self):
        print("call sub class constructor")

    def displayStudent(self):
        print("override parent class method")

sub1 = SeniorStudent()
sub1.displayStudent()