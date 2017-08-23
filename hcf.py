
class Student(object):
    '''student'''
    def __init__(self,name, marks):
        self.name = name
        self.mark = marks
        Student.number_of_student +=1

std1 = Student("silva", 100)
std2 = Student("programming", 50)

print(Student.number_of_student)
