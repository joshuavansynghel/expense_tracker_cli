from models.expense import Expense
from storage.expense_storage import ExpenseStorage
from utils.validation import validate_date, validate_amount

class ExpenseService:
    def __init__(self, expense_storage=None):
        self.expense_storage = expense_storage or ExpenseStorage()
        self.expenses = self.expense_storage.load_expenses()

    def get_expenses(self):
        return self.expenses

    def add_expense(self):
        # Ask user for input and validate 
        amount_text = input("What is the amount of the expense in euros?: ")
        amount = validate_amount(amount_text)

        date_text = input("What is the date of the expense?: ")
        dt = validate_date(date_text)

        category_text = input("What is the category of the expense?: ")
        description_text = input("What is the description of the expense?: ")

        # Instantiate expense
        expense = Expense(amount, dt, category_text, description_text)

        # Store locally and persistent
        self.expenses.append(expense)
        self.expense_storage.store_expenses(self.expenses)


    def filter_expenses(self, category):
        filtered_expenses = []

        for expense in self.expenses:
            if expense.category == category:
                filtered_expenses.append(expense)

        return filtered_expenses

    def calculate_summary(self, expenses):
        return sum(e.amount for e in expenses)