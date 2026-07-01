"""
config.py

Centralized configuration for the University Management System.
"""

from pathlib import Path

# ==========================
# Base Directories
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# ==========================
# Data Files
# ==========================

STUDENTS_FILE = DATA_DIR / "students.txt"
COURSES_FILE = DATA_DIR / "courses.txt"
LECTURERS_FILE = DATA_DIR / "lecturers.txt"
MODULES_FILE = DATA_DIR / "modules.txt"

GRADES_FILE = DATA_DIR / "grades.txt"
ATTENDANCE_FILE = DATA_DIR / "attendance.txt"
ENROLLMENTS_FILE = DATA_DIR / "enrollments.txt"

FEE_RECORDS_FILE = DATA_DIR / "fee_records.txt"
RECEIPTS_FILE = DATA_DIR / "receipts.txt"

REPORT_FILE = DATA_DIR / "report.txt"
ALL_DATA_FILE = DATA_DIR / "allData.txt"

# ==========================
# Authentication
# ==========================

ADMIN_PASSWORD = "adm1n"