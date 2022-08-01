class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания:" \
              f" {self.average_rate()}  \n Курсы в процессе изучения: {self.courses_in_progress}\n" \
              f" Завершенные курсы:{self.finished_courses}\n"
        return res

    def rate_hw(self, lecturer, course, grade):
        # считаем, что студент может оценивать лектора только по пройденому курсу
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        sum_rate = 0
        amount_rates = 0
        for rate in self.grades.values():
            sum_rate += sum(rate)
            amount_rates += len(rate)
        res = sum_rate / amount_rates
        return round(res,1)
    def __lt__(self, other):
        if isinstance(other, Student):
            if self.average_rate() > other.average_rate():
                return print(f'{self.name} круче!')
            elif self.average_rate() < other.average_rate():
                return print(f'{other.name} круче!')
            else:
                return print('Они равны')
        else:
            return 'Ошибка'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        res = f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rate()}\n"
        return res
    def average_rate(self):
        sum_rate = 0
        amount_rates = 0
        for rate in self.grades.values():
            sum_rate += sum(rate)
            amount_rates += len(rate)
        res = sum_rate / amount_rates
        return round(res,1)
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.average_rate() > other.average_rate():
                return print(f'{self.name} круче!')
            elif self.average_rate() < other.average_rate():
                return print(f'{other.name} круче!')
            else:
                return print('Они равны')
        else:
            return 'Ошибка'
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
        res = f" Имя: {self.name}\n Фамилия: {self.surname}\n"
        return res

best_student = Student('Ruoy', 'Eman', 'Chewbacca')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

worst_student = Student('Tyler', 'Durden', 'Male')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['Git']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

smart_Reviewer = Reviewer('Lucky', 'Strike')
smart_Reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Cooper', 'Super')
some_lecturer.courses_attached += ['Git']

other_lecturer = Lecturer('Robert', 'Bobert')
other_lecturer.courses_attached += ['Git']

cool_Reviewer.rate_hw(best_student, 'Python', 5)
cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 2)
cool_Reviewer.rate_hw(best_student, 'Python', 10)


smart_Reviewer.rate_hw(worst_student, 'Python', 2)
smart_Reviewer.rate_hw(worst_student, 'Python', 2)
smart_Reviewer.rate_hw(worst_student, 'Python', 2)
smart_Reviewer.rate_hw(worst_student, 'Python', 3)

best_student.rate_hw(some_lecturer, 'Git', 10)
best_student.rate_hw(some_lecturer, 'Git', 5)
best_student.rate_hw(some_lecturer, 'Git', 10)

worst_student.rate_hw(other_lecturer, 'Git', 10)
worst_student.rate_hw(other_lecturer, 'Git', 10)
worst_student.rate_hw(other_lecturer, 'Git', 10)

print(best_student)
print(best_student.grades)
print(worst_student)
print(cool_Reviewer)
print(smart_Reviewer)
print(some_lecturer)
print(other_lecturer)
some_lecturer < other_lecturer
best_student > worst_student

Student_list = [best_student, worst_student]
Lecturer_list = [some_lecturer, other_lecturer]

# Одна функция решает обе задачи
def av_rate_in_course(lists, course):
    sum_rate = 0
    amount_rates = 0
    for student in lists:
        for course_name, rate in student.grades.items():
            if course == course_name:
                sum_rate += sum(rate)
                amount_rates += len(rate)
                continue
    if amount_rates != 0:
        res = sum_rate / amount_rates
    else:
        return print('Ошибка!')
    return print(round(res,1))

av_rate_in_course(Student_list,'Python')
av_rate_in_course(Lecturer_list,'Git')
