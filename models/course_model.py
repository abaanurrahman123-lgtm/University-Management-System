from dataclasses import dataclass


@dataclass
class Course:
    course_id: str
    course_name: str
    duration: str

    @classmethod
    def from_record(cls, record):
        return cls(
            course_id=record[0],
            course_name=record[1],
            duration=record[2],
        )

    def to_record(self):
        return [
            self.course_id,
            self.course_name,
            self.duration,
        ]