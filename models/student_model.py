from dataclasses import dataclass


@dataclass
class Student:
    tp_number: str
    name: str
    program: str
    contact: str
    email: str
    birthday: str

    @classmethod
    def from_record(cls, record):
        return cls(
            tp_number=record[0],
            name=record[1],
            program=record[2],
            contact=record[3],
            email=record[4],
            birthday=record[5],
        )

    def to_record(self):
        return [
            self.tp_number,
            self.name,
            self.program,
            self.contact,
            self.email,
            self.birthday,
        ]