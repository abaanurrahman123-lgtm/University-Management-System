from models.course_model import Course

from repositories.course_repository import (
    add_course,
    get_course_by_id,
    save_course,
    course_exists,
)


def find_course(course_id):
    """
    Find a course by its ID.
    """
    return get_course_by_id(course_id)


def course_available(course_id):
    """
    Check if a course ID is available.
    """
    return not course_exists(course_id)


def register_course(course_data):
    """
    Register a new course.
    """
    course_id, course_name, course_credit = course_data

    if course_exists(course_id):
        return False, "Course ID already exists."

    course = Course(
        course_id,
        course_name,
        course_credit
    )

    add_course(course)

    return True, "Course added successfully."


def update_course(course_id, name=None, credit=None):
    """
    Update an existing course.
    """
    course = get_course_by_id(course_id)

    if course is None:
        return False, "Course not found."

    if name is not None:
        course.course_name = name

    if credit is not None:
        course.course_credit = credit

    save_course(course)

    return True, course