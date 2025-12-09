import csv
import os
from lab08.models import Student

headers = ['fio', 'birthdate', 'group', 'gpa']


class Group:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        '''создать файл с заголовком, если его ещё нет'''
        with open(self.storage_path, 'w', newline='', encoding='utf-8') as file:
            csv.writer(file).writerow(headers)

    def _read_all(self):
        '''прочитать все строки из CSV'''
        students = []
        with open(self.storage_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(
                    Student(fio=row["fio"], birthdate=row["birthdate"], group=row["group"], gpa=float(row["gpa"]), )
                )
        return students

    def _write(self, students):
        with open(self.storage_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for student in students:
                writer.writerow([student.fio, student.birthdate, student.group, student.gpa])


    def list(self):
        '''вернуть всех студентов в виде списка Student'''
        return self._read_all()

    def add(self, student: Student):
        '''добавить нового студента в CSV'''
        students = self._read_all()

        if any(student.fio == st.fio for st in students):
            raise ValueError('Такой студент уже есть')

        with open(self.storage_path, 'a', newline='', encoding='utf-8') as file:
            csv.writer(file).writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr: str):
        '''найти студентов по подстроке в fio'''
        students = self._read_all()
        for student in students:
            if substr.lower() in student.fio.lower():
                return student
            raise ValueError('Извините, такого студента нет в базе')

    def remove(self, fio: str):
        '''удалить запись(и) с данным fio'''
        students = self._read_all()
        new_list_students = []
        removed_count = 0

        for st in students:
            if st.fio.lower() != fio.lower():
                new_list_students.append(st)
            else:
                removed_count += 1

        if removed_count == 0:
            raise ValueError(f'студента с ФИО: {fio} нет в базе')

        self._write(new_list_students)

    def update(self, fio, **fields):
        '''обновить поля существующего студента'''
        students = self._read_all()
        update = False
        for st in students:
            if st.fio.lower() == fio.lower():
                for key, value in fields.items():
                    if 'fio' == key:
                        st.fio = value
                    if 'birthdate' == key:
                        st.birthdate = value
                    if 'group' == key:
                        st.group = value
                    if 'gpa' == key:
                        st.gpa = float(value)
                update = True
                break
        if update:
            self._write(students)
            return True

        return False


if __name__ == '__main__':
    student = Group('C:/Users/user/PycharmProjects/python_labs/data/lab09/students.csv')
    print(student.update('Ильин Илья Ильич', birthdate='2015-04-06', group='NEWGROUP'))
