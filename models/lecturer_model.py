from dataclasses import dataclass


@dataclass
class Lecturer:
    lecturer_id: str
    name: str
    contact: str

    @classmethod
    def from_record(cls, record):
        return cls(
            lecturer_id=record[0],
            name=record[1],
            contact=record[2],
        )

    def to_record(self):
        return [
            self.lecturer_id,
            self.name,
            self.contact,
        ]