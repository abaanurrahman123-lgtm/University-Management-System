from file_manager import (
    read_courses,
    write_courses,
)

from models.course_model import Course


def get_all_courses() -> list[Course]:
    """
    Return all courses.
    """
    records = read_courses()
    return [Course.from_record(record) for record in records]


def get_course_by_id(course_id: str) -> Course | None:
    """
    Find a course by its ID.
    """
    for course in get_all_courses():
        if course.course_id == course_id:
            return course
    return None


def save_all_courses(courses: list[Course]):
    """
    Save all courses.
    """
    records = [course.to_record() for course in courses]
    write_courses(records)


def add_course(course: Course):
    """
    Add a new course.
    """
    courses = get_all_courses()
    courses.append(course)
    save_all_courses(courses)


def save_course(updated_course: Course):
    """
    Update an existing course.
    """
    courses = get_all_courses()

    for i, course in enumerate(courses):
        if course.course_id == updated_course.course_id:
            courses[i] = updated_course
            break

    save_all_courses(courses)


def course_exists(course_id: str) -> bool:
    """
    Check if a course already exists.
    """
    return get_course_by_id(course_id) is not None

def delete_course(course_id):
    """
    Delete a course by its ID.
    """
    courses = get_all_courses()

    courses = [
        course
        for course in courses
        if course.course_id != course_id
    ]

    save_all_courses(courses)