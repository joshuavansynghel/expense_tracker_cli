from datetime import date

class Expense:
    def __init__(self, amount:float, date:date, category:str, description:str) -> None:
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.date} | €{self.amount:.2f} | {self.category} | {self.description}"