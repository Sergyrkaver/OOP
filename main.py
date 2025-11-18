class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'

        if (course in self.courses_in_progress and
                course in lecturer.courses_attached and
                1 <= grade <= 10):

            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() < other._get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() <= other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() == other._get_avg_grade()

    def _get_avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        # Вычисляем среднюю оценку за лекции
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() < other._get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() <= other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() == other._get_avg_grade()

    def _get_avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):

            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

print('Проверяющий')
some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)
print()

print('Лектор')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [9, 10, 9.5]}
print(some_lecturer)
print()

print('Студент')
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades = {'Python': [10, 9, 10]}
print(some_student)
print()

print('Сравнение лекторов')
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.grades = {'Python': [8, 9, 7]}
lecturer2 = Lecturer('Петр', 'Петров')
lecturer2.grades = {'Java': [9, 10, 9]}

print(f"Лектор 1 средняя: {lecturer1._get_avg_grade():.1f}")
print(f"Лектор 2 средняя: {lecturer2._get_avg_grade():.1f}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
print()

print('Сравнение студентов')
student1 = Student('Иван', 'Петров', 'М')
student1.grades = {'Python': [7, 8, 9]}
student2 = Student('Ольга', 'Кузнецова', 'Ж')
student2.grades = {'Java': [9, 10, 9]}

print(f"Студент 1 средняя: {student1._get_avg_grade():.1f}")
print(f"Студент 2 средняя: {student2._get_avg_grade():.1f}")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")