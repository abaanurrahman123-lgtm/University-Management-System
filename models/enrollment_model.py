from dataclasses import dataclass


@dataclass
class Enrollment:
    student_id: str
    module_code: str

    @classmethod
    def from_record(cls, record):
        return cls(
            student_id=record[0],
            module_code=record[1],
        )

    def to_record(self):
        return [
            self.student_id,
            self.module_code,
        ]