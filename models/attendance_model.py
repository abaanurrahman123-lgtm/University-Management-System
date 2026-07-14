from dataclasses import dataclass


@dataclass
class Attendance:
    date: str
    module_code: str
    student_id: str
    status: str

    @classmethod
    def from_record(cls, record):
        return cls(
            date=record[0],
            module_code=record[1],
            student_id=record[2],
            status=record[3],
        )

    def to_record(self):
        return [
            self.date,
            self.module_code,
            self.student_id,
            self.status,
        ]