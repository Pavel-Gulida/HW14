
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age} age, {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.record_book = record_book

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age} age, {self.gender}, {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise ValueError("Max student")
        self.group.add(student)

    def delete_student(self, last_name):
        student = 0
        for el in self.group:
            if el.last_name == last_name:
                student = el
        self.group.discard(student)


    def find_student(self, last_name):
        for el in self.group:
            if el.last_name == last_name:
                return el

    def __str__(self):
        all_students = ""
        for el in self.group:
            all_students += str(el) + "\n"
        return f'Number: {self.number}\n{all_students}'


gr = Group('PD1')

try:
    for _ in range(11):
        gr.add_student(Student('Male', 30, 'Steve', 'Jobs', 'AN142'))
except ValueError as error:
    print(error)




