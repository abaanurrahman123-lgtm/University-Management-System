from repositories.student_repository import (
    add_student,
    get_student_by_tp,
    save_student,
    student_exists,
    email_exists,
)

from models.student_model import Student

from repositories.student_repository import get_student_by_tp


def find_student(tp_number: str):
    """
    Find a student by TP number.
    """
    return get_student_by_tp(tp_number)

from repositories.student_repository import (
    student_exists,
    email_exists,
)

def can_register_student(tp_number: str, email: str) -> tuple[bool, str]:
    """
    Validate whether a student can be registered.
    """

    if student_exists(tp_number):
        return False, "TP number already exists."

    if email_exists(email):
        return False, "Email already exists."

    return True, ""