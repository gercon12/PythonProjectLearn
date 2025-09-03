class Teacher():
    def __init__(self, grade):
        #print("teacher")
        self.grade = grade
    def degree(self):
        print("teach")

class Youtuber():
    def __init__(self, grade):
        self.grade = grade
        #print("youtube")
    def degree(self):
        print("youtube")

class Student(Teacher, Youtuber):
    def __init__(self, grade):
        super().__init__(grade)
        #print("student")
    def degree(self):
        print("student")
        Teacher.degree(self)
        Youtuber.degree(self)

s = Student("Master student")
s.degree()






