from dataclasses import dataclass


@dataclass
class FeeRecord:
    student_id: str
    student_name: str
    amount_paid: str
    outstanding_balance: str
    payment_date: str

    @classmethod
    def from_record(cls, record):
        return cls(
            student_id=record[0],
            student_name=record[1],
            amount_paid=record[2],
            outstanding_balance=record[3],
            payment_date=record[4],
        )

    def to_record(self):
        return [
            self.student_id,
            self.student_name,
            self.amount_paid,
            self.outstanding_balance,
            self.payment_date,
        ]