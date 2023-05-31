from utils import get_student_by_pk, get_profession, get_student


def main():
    user_pk: int = int(input('Введите номер студента\n'))
    student: dict = get_student_by_pk(user_pk)
    stud_info = get_student(student)
    print(stud_info['result'])
    print(get_profession(student)) if stud_info['check'] else None


if __name__ == '__main__':
    main()