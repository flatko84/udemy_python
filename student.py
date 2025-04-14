import random

class Student:
    educational_platform = 'udemy'
    _greetings = [
        'Hi, I\'m {}',
        'Hi there, my name is {}',
        'Hi. Oh, my name is {}'
    ]

    def __init__(self, name, age = 10):
        self.name = name
        self.age = age

    def greet(self):
        rnd = random.randrange(0, len(self._greetings))
        return self._greetings[rnd].format(self.name)
    

student_names = ['Sasho', 'Pesho', 'Gosho', 'Tosho']
students = []

for student_name in student_names:
    students.append(Student(student_name))

for student in students:
    print(student.greet())