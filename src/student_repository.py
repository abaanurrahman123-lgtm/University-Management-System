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