from dataclasses import dataclass


@dataclass
class Course:
    course_id: str
    course_name: str
    course_credit: int

    @classmethod
    def from_record(cls, record):
        return cls(
            course_id=record[0],
            course_name=record[1],
            course_credit=(record[2]),
        )

    def to_record(self):
        return [
            self.course_id,
            self.course_name,
            self.course_credit,
        ]