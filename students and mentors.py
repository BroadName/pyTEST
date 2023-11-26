class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __gt__(self, other):
        return self.avg() > other.avg()

    def __lt__(self, other):
        return self.avg() < other.avg()

    def __ge__(self, other):
        return self.avg() >= other.avg()

    def __le__(self, other):
        return self.avg() <= other.avg()

    def __eq__(self, other):
        return  self.avg() == other.avg()

    def __ne__(self, other):
        return self.avg() != other.avg()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg(self):
        if len(self.grades) == 0:
            return 'Студент не имеет оценок'
        sum_ = 0
        len_ = 0
        for i in self.grades.values():
            for j in i:
                sum_ += j
                len_ += 1
        return sum_/len_

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg()}' \
               f'\nКурсы в процессе изучения: {", ".join(str(i) for i in self.courses_in_progress)}' \
               f'\nЗавершённые курсы: {" ".join(str(i) for i in self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg(self):
        if len(self.grades) == 0:
            return 'Лектор не имеет оценок'
        sum_ = 0
        len_ = 0
        for i in self.grades.values():
            for j in i:
                sum_ += j
                len_ += 1
        return sum_/len_

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg()}"

    def __gt__(self, other):
        return self.avg() > other.avg()

    def __lt__(self, other):
        return self.avg() < other.avg()

    def __ge__(self, other):
        return self.avg() >= other.avg()

    def __le__(self, other):
        return self.avg() <= other.avg()

    def __eq__(self, other):
        return  self.avg() == other.avg()

    def __ne__(self, other):
        return self.avg() != other.avg()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


first_lecturer = Lecturer('George', 'Orwell')
first_lecturer.courses_attached += ['History']

second_lecturer = Lecturer('Leonid', 'Parfenof')
second_lecturer.courses_attached += ['History']

lazy_student = Student('Adolf', 'Hitler', 'male')
lazy_student.courses_in_progress += ['History']
lazy_student.courses_in_progress += ['Git']
lazy_student.courses_in_progress += ['Python']
lazy_student.rate_lecturer(first_lecturer, 'History', 2)
lazy_student.rate_lecturer(first_lecturer, 'History', 3)
lazy_student.rate_lecturer(second_lecturer, 'History', 6)
lazy_student.rate_lecturer(second_lecturer, 'History', 5)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(lazy_student, 'Python', 9)
cool_mentor.rate_hw(lazy_student, 'Python', 9)

sad_mentor = Reviewer('Filip', 'Voronin')
sad_mentor.courses_attached += ['Git']
sad_mentor.rate_hw(lazy_student, 'Git', 5)
sad_mentor.rate_hw(lazy_student, 'Git', 8)

l_students = [best_student, lazy_student]
l_lecturers = [first_lecturer, second_lecturer]


def average_stud(list_students, course):
    sum_rates = 0
    count = 0
    for i in list_students:
        if isinstance(i, Student) and course in i.courses_in_progress:
            sum_rates += sum(i.grades[course])
            count += len(i.grades[course])
    return sum_rates/count


def average_lecturer(list_lecturers, course):
    sum_rates = 0
    count = 0
    for i in list_lecturers:
        if isinstance(i, Lecturer) and course in i.courses_attached:
            sum_rates += sum(i.grades[course])
            count += len(i.grades[course])
    return sum_rates/count


print(first_lecturer != second_lecturer)
print(best_student == lazy_student)
print(average_lecturer(l_lecturers, 'History'))
print(average_stud(l_students, 'Python'))
print(lazy_student.avg())
print(first_lecturer.avg())
print(best_student.__dict__)
print(lazy_student.__dict__)
print(cool_mentor.__dict__)
print(first_lecturer.__dict__)
print(lazy_student.__dict__)
print()
print(best_student)
print()
print(first_lecturer)
print()
print(cool_mentor)
