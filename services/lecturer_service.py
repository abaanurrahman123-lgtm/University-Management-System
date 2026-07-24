from models.lecturer_model import Lecturer

from repositories.lecturer_repository import (
    add_lecturer,
    get_lecturer_by_id,
    save_lecturer,
    lecturer_exists,
)


def find_lecturer(lecturer_id):
    """
    Find a lecturer by ID.
    """
    return get_lecturer_by_id(lecturer_id)


def lecturer_available(lecturer_id):
    """
    Check if a lecturer ID is available.
    """
    return not lecturer_exists(lecturer_id)


def register_lecturer(lecturer_data):
    """
    Register a new lecturer.
    """
    lecturer_id, lecturer_name, lecturer_contact = lecturer_data

    if lecturer_exists(lecturer_id):
        return False, "Lecturer ID already exists."

    lecturer = Lecturer(
        lecturer_id,
        lecturer_name,
        lecturer_contact
    )

    add_lecturer(lecturer)

    return True, "Lecturer added successfully."


def update_lecturer(lecturer_id, name=None, contact=None):
    """
    Update an existing lecturer.
    """
    lecturer = get_lecturer_by_id(lecturer_id)

    if lecturer is None:
        return False, "Lecturer not found."

    if name is not None:
        lecturer.lecturer_name = name

    if contact is not None:
        lecturer.lecturer_contact = contact

    save_lecturer(lecturer)

    return True, lecturer