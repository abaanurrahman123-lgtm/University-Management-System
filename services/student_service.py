from repositories.student_repository import (
    add_student,
    get_student_by_tp,
    save_student,
    student_exists,
    email_exists,
)

from models.student_model import Student

def find_student(tp_number: str) -> Student | None:
    """
    Find a student by TP number.
    """
    return get_student_by_tp(tp_number)

def can_register_student(tp_number: str, email: str) -> tuple[bool, str]:
    """
    Validate whether a student can be registered.
    """

    if student_exists(tp_number):
        return False, "TP number already exists."

    if email_exists(email):
        return False, "Email already exists."

    return True, ""

def register_student(student_data: tuple) -> tuple[bool, str]:
    """
    Register a new student.

    student_data should be:
    (tp_number, name, program, contact, email, birthday)
    """

    tp_number, name, program, contact, email, birthday = student_data

    valid, message = can_register_student(tp_number, email)

    if not valid:
        return False, message

    student = Student(
        tp_number=tp_number,
        name=name,
        program=program,
        contact=contact,
        email=email,
        birthday=birthday,
    )

    add_student(student)

    return True, "Student registered successfully."

def update_student(
    tp_number: str,
    program: str | None = None,
    contact: str | None = None,
    email: str | None = None,
) -> tuple[bool, str]:
    """
    Update an existing student's information.
    """

    student = get_student_by_tp(tp_number)

    if student is None:
        return False, "Student not found."

    if program is not None:
        student.program = program

    if contact is not None:
        student.contact = contact

    if email is not None:
        if student.email != email and email_exists(email):
            return False, "Email already exists."

        student.email = email

    save_student(student)

    return True, "Student updated successfully."

def email_available(email: str) -> bool:
    """
    Check whether an email is available for registration.
    """
    return not email_exists(email)