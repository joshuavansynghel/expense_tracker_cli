from datetime import date

class Expense:
    def __init__(self, amount:float, date:date, category:str, description:str) -> None:
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description


    def to_dict(self):
        return {
            'amount': self.amount,
            'date': self.date,
            'category': self.category,
            'description': self.description
        }


    def from_dict(self, dict):
        return Expense(
            dict['amount'],
            dict['date'],
            dict['category'],
            dict['description']
        )


    def __str__(self):
        return f'{self.date} | €{self.amount:.2f} | {self.category} | {self.description}'