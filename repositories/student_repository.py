from file_manager import read_students, write_students
from models.student_model import Student


def get_all_students() -> list[Student]:
    """
    Return all students as Student objects.
    """
    return [
        Student.from_record(record)
        for record in read_students()
    ]


def save_all_students(students: list[Student]) -> None:
    """
    Save Student objects back to storage.
    """
    write_students(
        [
            student.to_record()
            for student in students
        ]
    )

def get_student_by_tp(tp_number):
    """
    Return one Student object by TP number.
    """
    for student in get_all_students():
        if student.tp_number == tp_number:
            return student

    return None

def save_student(updated_student):
    """
    Update one student and save.
    """

    students = get_all_students()

    for i, student in enumerate(students):
        if student.tp_number == updated_student.tp_number:
            students[i] = updated_student
            break

    save_all_students(students)

def add_student(student):
    """
    Add a new Student object.
    """
    students = get_all_students()
    students.append(student)
    save_all_students(students)

def student_exists(tp_number):
    """
    Check whether a student exists.
    """
    return get_student_by_tp(tp_number) is not None

def email_exists(email):
    """
    Check whether an email already exists.
    """
    return any(
        student.email == email
        for student in get_all_students()
    )