import json
from pathlib import Path
from models import Student


students_data = [
    Student('Ильин Илья Ильич', '2005-01-02', 'BIVT-24-3', 3.6),
    Student('Федин Фёдор Фёдорович', '2006-08-23', 'BIVT-21-16', 4.5)
]

def students_to_json(students, path):
    p = Path(path)
    data = [s.to_dict() for s in students]
    with open(str(p), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def students_from_json(path):
    p = Path(path)
    with open(str(p), 'r') as file:
        data = json.load(file)
    print([Student.from_dict(item) for item in data])


if __name__ == '__main__':
    students_to_json(students_data, 'C:/Users/matve/PycharmProjects/python_labs/data/lab08/students_output.json')
    students_from_json('C:/Users/matve/PycharmProjects/python_labs/data/lab08/students_input.json')