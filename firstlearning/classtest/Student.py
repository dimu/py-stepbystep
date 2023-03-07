class Student:
    """student class containes name and sex"""

    studentCount = 0

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Student.studentCount += 1

    def displayStudent(self):
        print("name:", self.name, ",sex:", self.sex)

    def displayStudentCount(self):
        print("Total student:", Student.studentCount)


lily = Student("lily", "female")
tom = Student("tom", "male")

lily.displayStudent()
lily.displayStudentCount()
tom.displayStudent()
tom.displayStudentCount()

# use attr method to access object's attribute
# check if has some attribute
print(hasattr(lily, "name"))

# get attribute value
print(getattr(lily, "name", "lucy"))

# add attribute
print(setattr(lily, "score", 100))
print(getattr(lily, "score"))

# delete attribute
print(delattr(lily, "name"))
# erase an error: Student object has no attribute name
# print(lily.displayStudent())

# built-in class attribute
print("doc:", Student.__doc__)
print("name:", Student.__name__, "module:", Student.__module__, "dict:", Student.__dict__)


# reference count test
stu1 = Student("tom", "boy")
stu2 = stu1
stu3 = stu1
print(id(stu1), id(stu2), id(stu3))
del stu1
del stu2
del stu3
