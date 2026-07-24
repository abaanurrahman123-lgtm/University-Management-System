from file_manager import (
    read_lecturers,
    write_lecturers,
)

from models.lecturer_model import Lecturer


def get_all_lecturers() -> list[Lecturer]:
    """
    Return all lecturers.
    """
    records = read_lecturers()
    return [Lecturer.from_record(record) for record in records]


def get_lecturer_by_id(lecturer_id: str) -> Lecturer | None:
    """
    Find a lecturer by ID.
    """
    for lecturer in get_all_lecturers():
        if lecturer.lecturer_id == lecturer_id:
            return lecturer
    return None


def save_all_lecturers(lecturers: list[Lecturer]):
    """
    Save all lecturers.
    """
    records = [lecturer.to_record() for lecturer in lecturers]
    write_lecturers(records)


def add_lecturer(lecturer: Lecturer):
    """
    Add a new lecturer.
    """
    lecturers = get_all_lecturers()
    lecturers.append(lecturer)
    save_all_lecturers(lecturers)


def save_lecturer(updated_lecturer: Lecturer):
    """
    Update an existing lecturer.
    """
    lecturers = get_all_lecturers()

    for i, lecturer in enumerate(lecturers):
        if lecturer.lecturer_id == updated_lecturer.lecturer_id:
            lecturers[i] = updated_lecturer
            break

    save_all_lecturers(lecturers)


def lecturer_exists(lecturer_id: str) -> bool:
    """
    Check if a lecturer already exists.
    """
    return get_lecturer_by_id(lecturer_id) is not None