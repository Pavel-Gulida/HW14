
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
