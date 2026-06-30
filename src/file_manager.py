"""
file_manager.py

Centralized file operations for the University Management System.
"""

from pathlib import Path
from config import *

# ==================================================
# Generic File Functions
# ==================================================

def read_lines(file_path):
    """
    Read all lines from a file.

    Returns:
        list[str]
    """
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_lines(file_path, lines):
    """
    Write a list of lines to a file.
    """
    with open(file_path, "w") as file:
        file.writelines(lines)


def append_line(file_path, line):
    """
    Append one line to a file.
    """
    with open(file_path, "a") as file:
        file.write(line + "\n")

# ==================================================
# Student File Operations
# ==================================================

def read_students():
    """
    Read all student records.
    """
    return read_lines(STUDENTS_FILE)


def write_students(lines):
    """
    Overwrite all student records.
    """
    write_lines(STUDENTS_FILE, lines)


def append_student(student):
    """
    Add a new student record.
    """
    append_line(STUDENTS_FILE, student)

# ==================================================
# Course File Operations
# ==================================================

def read_courses():
    """
    Read all course records.
    """
    return read_lines(COURSES_FILE)


def write_courses(lines):
    """
    Overwrite all course records.
    """
    write_lines(COURSES_FILE, lines)


def append_course(course):
    """
    Add a new course record.
    """
    append_line(COURSES_FILE, course)

# ==================================================
# Lecturer File Operations
# ==================================================

def read_lecturers():
    """
    Read all lecturer records.
    """
    return read_lines(LECTURERS_FILE)


def write_lecturers(lines):
    """
    Overwrite all lecturer records.
    """
    write_lines(LECTURERS_FILE, lines)


def append_lecturer(lecturer):
    """
    Add a new lecturer record.
    """
    append_line(LECTURERS_FILE, lecturer)

# ==================================================
# Module File Operations
# ==================================================

def read_modules():
    """
    Read all module records.
    """
    return read_lines(MODULES_FILE)


def write_modules(lines):
    """
    Overwrite all module records.
    """
    write_lines(MODULES_FILE, lines)


def append_module(module):
    """
    Add a new module record.
    """
    append_line(MODULES_FILE, module)

# ==================================================
# Grade File Operations
# ==================================================

def read_grades():
    """
    Read all grade records.
    """
    return read_lines(GRADES_FILE)


def write_grades(lines):
    """
    Overwrite all grade records.
    """
    write_lines(GRADES_FILE, lines)


def append_grade(grade):
    """
    Add a new grade record.
    """
    append_line(GRADES_FILE, grade)

# ==================================================
# Attendance File Operations
# ==================================================

def read_attendance():
    """
    Read all attendance records.
    """
    return read_lines(ATTENDANCE_FILE)


def write_attendance(lines):
    """
    Overwrite all attendance records.
    """
    write_lines(ATTENDANCE_FILE, lines)


def append_attendance(record):
    """
    Add a new attendance record.
    """
    append_line(ATTENDANCE_FILE, record)