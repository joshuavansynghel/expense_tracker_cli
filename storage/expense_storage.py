import os
import json

from pathlib import Path

from models.expense import Expense

class ExpenseStorage:

    def __init__(self, file_path="data/expenses.json"):
        self.file_path = Path(file_path)

    def store_expenses(self, expenses):
         # Ensure directory exists
         self.file_path.parent.mkdir(parents=True, exist_ok=True)

         with self.file_path.open("w") as f:
             json.dump(
                [Expense.to_dict(e) for e in expenses], 
                f,
                indent=4,
                default=str
            )

    def load_expenses(self, default=None):
        if default == None:
            default = []

        try:
            with self.file_path.open("r") as f:
                data =  json.load(f)
            
            return [Expense.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError) :
            return default