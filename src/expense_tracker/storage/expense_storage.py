import os
import json

from pathlib import Path

from expense_tracker.models.expense import Expense

class ExpenseStorage:

    def __init__(self, data_file: Path):
        self.data_file = data_file

    def store_expenses(self, expenses):
         # Ensure directory exists
         self.data_file.parent.mkdir(parents=True, exist_ok=True)

         with self.data_file.open("w") as f:
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
            with self.data_file.open("r") as f:
                data =  json.load(f)
            
            return [Expense.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError) :
            return default