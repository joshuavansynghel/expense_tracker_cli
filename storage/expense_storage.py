import os
import json

class ExpenseStorage:

    def __init__(self, file_path="../data"):
        self.file_path = file_path

    def store_expenses(self, expenses):
        file_location = os.path.join(self.file_path, "expenses.json")

        with open(file_location, "w") as f:
            json.dump(expenses, f)

    def load_expenses(self):
        file_location = os.path.join(self.file_path, "expenses.json")

        with open(file_location, "r") as f:
            expenses = json.load(f)

        return expenses