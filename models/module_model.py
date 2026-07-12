from dataclasses import dataclass


@dataclass
class Module:
    module_code: str
    module_name: str
    course_id: str
    lecturer_id: str

    @classmethod
    def from_record(cls, record):
        return cls(
            module_code=record[0],
            module_name=record[1],
            course_id=record[2],
            lecturer_id=record[3],
        )

    def to_record(self):
        return [
            self.module_code,
            self.module_name,
            self.course_id,
            self.lecturer_id,
        ]