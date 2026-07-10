from file_manager import read_students, write_students
from models.student_model import Student


def get_all_students():
    """
    Return all students as Student objects.
    """
    return [
        Student.from_record(record)
        for record in read_students()
    ]


def save_all_students(students):
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
