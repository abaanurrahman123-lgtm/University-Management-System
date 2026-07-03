"""
file_manager.py

Centralized file operations for the University Management System.
"""

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

def read_records(file_path):
    """
    Read a text file and return a list of records.

    Each record is returned as a list of values.
    """
    return [
        line.strip().split(", ")
        for line in read_lines(file_path)
        if line.strip()
    ]


def write_records(file_path, records):
    """
    Save a list of records to a text file.
    """
    lines = [
        ", ".join(record) + "\n"
        for record in records
    ]
    write_lines(file_path, lines)

# ==================================================
# Student File Operations
# ==================================================

def read_students():
    return read_records(STUDENTS_FILE)


def write_students(records):
    write_records(STUDENTS_FILE, records)


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
    return read_records(COURSES_FILE)


def write_courses(records):
    """
    Overwrite all course records.
    """
    write_records(COURSES_FILE, records)


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
    return read_records(LECTURERS_FILE)


def write_lecturers(records):
    """
    Overwrite all lecturer records.
    """
    write_records(LECTURERS_FILE, records)


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
    return read_records(MODULES_FILE)


def write_modules(records):
    """
    Overwrite all module records.
    """
    write_records(MODULES_FILE, records)


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
    return read_records(GRADES_FILE)


def write_grades(records):
    """
    Overwrite all grade records.
    """
    write_records(GRADES_FILE, records)


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
    return read_records(ATTENDANCE_FILE)


def write_attendance(records):
    """
    Overwrite all attendance records.
    """
    write_records(ATTENDANCE_FILE, records)


def append_attendance(record):
    """
    Add a new attendance record.
    """
    append_line(ATTENDANCE_FILE, record)

# ==================================================
# Enrollment File Operations
# ==================================================

def read_enrollments():
    """
    Read all enrollment records.
    """
    return read_records(ENROLLMENTS_FILE)


def write_enrollments(records):
    """
    Overwrite all enrollment records.
    """
    write_records(ENROLLMENTS_FILE, records)


def append_enrollment(record):
    """
    Add a new enrollment record.
    """
    append_line(ENROLLMENTS_FILE, record)

# ==================================================
# Fee Record Operations
# ==================================================

def read_fee_records():
    """
    Read all fee records.
    """
    return read_records(FEE_RECORDS_FILE)


def write_fee_records(records):
    """
    Overwrite all fee records.
    """
    write_records(FEE_RECORDS_FILE, records)


def append_fee_record(record):
    """
    Add a new fee record.
    """
    append_line(FEE_RECORDS_FILE, record)

# ==================================================
# Receipt File Operations
# ==================================================

def read_receipts():
    """
    Read all receipts.
    """
    return read_records(RECEIPTS_FILE)


def write_receipts(records):
    """
    Overwrite all receipts.
    """
    write_records(RECEIPTS_FILE, records)


def append_receipt(receipt):
    """
    Add a new receipt.
    """
    append_line(RECEIPTS_FILE, receipt)

# ==================================================
# Report File Operations
# ==================================================

def write_report(lines):
    """
    Save the generated report.
    """
    write_lines(REPORT_FILE, lines)

# ==================================================
# All Data File Operations
# ==================================================

def write_all_data(lines):
    """
    Save the combined data report.
    """
    write_lines(ALL_DATA_FILE, lines)