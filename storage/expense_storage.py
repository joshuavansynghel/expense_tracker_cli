import os
import json

from pathlib import Path

class ExpenseStorage:

    def __init__(self, file_path="../data/expenses.json"):
        self.file_path = Path(file_path)

    def store_expenses(self, expenses):
         # Ensure directory exists
         self.file_path.parent.mkdir(parents=True, exist_ok=True)

         with self.file_path.open("w") as f:
             json.dump(expenses, f)

    def load_expenses(self, default=None):
        if default == None:
            default = []

        try:
            with self.file_path.open("r") as f:
                return json.load(f)
        except FileNotFoundError:
            return default