#Non-OOP
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence) if len(sequence) > 0 else 0

print(average(student["grades"]))
print('----------')
#OOP
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0

student = Student("Bob", (100, 85, 95, 80, 91))
print(student.name)
print(student.grades)
print(student.average_grade())
print("\n")
student2 = Student("Rolf", (89, 90, 93, 78, 90))
print(student2.name)
print(student2.grades)
print(student2.average_grade())

