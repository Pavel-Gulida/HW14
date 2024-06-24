
from human import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.record_book = record_book

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age} age, {self.gender}, {self.record_book}"