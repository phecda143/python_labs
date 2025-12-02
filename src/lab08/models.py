from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, '%Y-%m-%d')
        except ValueError:
            raise ValueError('дата рождения должна быть в формате YYYY-MM-DD')

        if date.today().year < int(self.birthdate.split('-')[0]):
            raise ValueError('Год рождения не может быть больше чем текущий год')

        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError('gpa должен находиться в промежутке от 0 до 5')

        if isinstance(self.gpa, int):
            raise ValueError('gpa должен быть в формате float')

    def age(self) -> int:
        '''возвращает количество полных лет'''
        return date.today().year - int(self.birthdate.split('-')[0])

    def to_dict(self) -> dict:
        '''сериализация объекта в словарь'''
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fio=data['fio'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=data['gpa']
        )

    def __str__(self):
        '''красивый вывод'''
        return f'ФИО студента: {self.fio}\n Дата рождения: {self.birthdate}\n Возраст: {self.age()}\n Группа: {self.gpa}\n GPA: {self.gpa}'


# if __name__ == '__main__':
#     student = Student(
#         fio = 'Александров Александр Александрович',
#         birthdate = '2006-01-25',
#         group = 'BIVT-25-2',
#         gpa = 4.7
#     )
#     print(student.to_dict()) # вывод в виде словаря
#     print()
#     print(student.from_dict(student.to_dict())) # вывод в красивом виде из словаря
#     print()
#     print(student.age()) # вывод полных лет
#     print()
#     print(student) # вывод в красивом виде
