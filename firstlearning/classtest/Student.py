class Student:
    'student class containes name and sex'

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