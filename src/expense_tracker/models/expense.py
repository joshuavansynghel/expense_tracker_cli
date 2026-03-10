import itertools

from datetime import date

from expense_tracker.utils.validation import validate_amount, validate_date

class Expense:

    id_iter = itertools.count(1)

    def __init__(self, amount:float, date:date, category:str, description:str) -> None:
        self.id = next(Expense.id_iter)
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description


    def to_dict(self):
        return {
            'id': self.id,
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