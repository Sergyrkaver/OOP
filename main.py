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


def calculate_avg_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])

    return sum(total_grades) / len(total_grades) if total_grades else 0


def calculate_avg_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])

    return sum(total_grades) / len(total_grades) if total_grades else 0



print('Создаем экземпляры')

reviewer1 = Reviewer('Петр', 'Петров')
reviewer2 = Reviewer('Мария', 'Сидорова')

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Анна', 'Кузнецова')

student1 = Student('Алексей', 'Смирнов', 'М')
student2 = Student('Ольга', 'Орлова', 'Ж')

print('Настройка курсов')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2.courses_in_progress = ['Python', 'Java']
student2.finished_courses = ['Основы алгоритмов']

lecturer1.courses_attached = ['Python', 'Git']
lecturer2.courses_attached = ['Python', 'Java']

reviewer1.courses_attached = ['Python', 'Git']
reviewer2.courses_attached = ['Python', 'Java']

print('Выставления оценок студентам')
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 10)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Java', 8)

print('Оценки студента 1:', student1.grades)
print('Оценки студента 2:', student2.grades)

print('Выставления оченок лекторам')
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 8)

student2.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Java', 9)

print('Оценки лектора 1:', lecturer1.grades)
print('Оценки лектора 2:', lecturer2.grades)

print('Тестирование магических методов')
print('Reviewer 1:')
print(reviewer1)
print('Reviewer 2:')
print(reviewer2)

print('Lecturer 1:')
print(lecturer1)
print('Lecturer 2:')
print(lecturer2)

print('Student 1:')
print(student1)
print('Student 2:')
print(student2)

print('Тестирование сравнений')
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 <= student2: {student1 <= student2}")

print('Тестирование функций')
# Тестируем функции подсчета средних оценок
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

python_avg_hw = calculate_avg_hw_grade(students_list, 'Python')
python_avg_lecture = calculate_avg_lecture_grade(lecturers_list, 'Python')

print(f"Средняя оценка за ДЗ по курсу Python: {python_avg_hw:.1f}")
print(f"Средняя оценка за лекции по курсу Python: {python_avg_lecture:.1f}")

git_avg_hw = calculate_avg_hw_grade(students_list, 'Git')
java_avg_lecture = calculate_avg_lecture_grade(lecturers_list, 'Java')

print(f"Средняя оценка за ДЗ по курсу Git: {git_avg_hw:.1f}")
print(f"Средняя оценка за лекции по курсу Java: {java_avg_lecture:.1f}")

print('Тестирование ошибок')
print("Ошибка при оценке не того курса:", reviewer1.rate_hw(student1, 'Java', 8))
print("Ошибка при оценке не лектора:", student1.rate_lecture(reviewer1, 'Python', 8))
print("Ошибка при оценке несуществующего курса:", student1.rate_lecture(lecturer1, 'C++', 8))