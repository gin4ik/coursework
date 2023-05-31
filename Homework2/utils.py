import json

from settings import STUDENT_PATH, PROF_PATH

def load_file(path: str) -> list[dict]:
    with open(path) as file:
        return json.load(file)

def get_student_by_pk(pk: int) -> dict | None:
    students = load_file(STUDENT_PATH)
    for student in students:
        if student['pk'] == pk:
            return student


def get_profession_by_title(title: str) -> dict | None:
    professions = load_file(PROF_PATH)
    for profession in professions:
        if profession['title'].lower() == title.lower():
            return profession


def check_fitness(student: dict, profession: dict) -> dict:
    has = set(student['skills']) & set(profession['skills'])
    lacks = set(profession['skills']) - set(student['skills'])
    fit_percent = int(len(has) / len(profession['skills']) * 100)
    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent
    }


def get_student(student: dict) -> dict:
    if student:
        return {'result': f'Студент {student["full_name"]}\nЗнает {", ".join(student["skills"])}', 'check': True}
    return {'result': 'У нас нет такого студента', 'check': False}


def get_profession(student: dict) -> str:
    prof_title: str = input(f'Выберите специальность для оценки студента {student["full_name"]}\n')
    profession: dict | None = get_profession_by_title(prof_title)
    if profession:
        statistic: dict = check_fitness(student, profession)
        return f'Пригодность {statistic["fit_percent"]}%\n{student["full_name"]} знает {", ".join(statistic["has"])}\n' \
               f'{student["full_name"]} не знает {", ".join(statistic["lacks"])}'
    return 'У нас нет такой специальности'
