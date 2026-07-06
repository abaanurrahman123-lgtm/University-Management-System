from dataclasses import dataclass


@dataclass
class Student:
    tp_number: str
    name: str
    program: str
    contact: str
    email: str
    birthday: str