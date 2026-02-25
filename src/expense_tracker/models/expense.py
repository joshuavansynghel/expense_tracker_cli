from datetime import date

from expense_tracker.utils.validation import validate_amount, validate_date

class Expense:
    def __init__(self, amount:float, date:date, category:str, description:str) -> None:
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description


    def to_dict(self):
        return {
            'amount': self.amount,
            'date': self.date.isoformat(),
            'category': self.category,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, dict):
        return Expense(
            validate_amount(dict['amount']),
            validate_date(dict['date']),
            dict['category'],
            dict['description']
        )


    def __str__(self):
        return f'{self.date} | €{self.amount:.2f} | {self.category} | {self.description}'