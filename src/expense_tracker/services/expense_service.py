from expense_tracker.models.expense import Expense
from expense_tracker.storage.expense_storage import ExpenseStorage
from expense_tracker.config.settings import EXPENSES_PATH


class ExpenseService:

    def __init__(self, expense_storage=None):
        self.expense_storage = expense_storage or ExpenseStorage(EXPENSES_PATH)
        self.expenses = self.expense_storage.load_expenses()


    def get_expenses(self):
        return self.expenses


    def add_expense(self, amount, date, category, description):
    
        # Instantiate expense
        expense = Expense(amount, date, category, description)

        # Store locally and persistent
        self.expenses.append(expense)
        self.expense_storage.store_expenses(self.expenses)

    
    def delete_expense(self, id):
        for i, _ in enumerate(self.expenses):
            if self.expenses[i].id == id:
                del self.expenses[i]
                self.expense_storage.store_expenses(self.expenses)
                return True
        return False




    def filter_expenses(self, category):
        filtered_expenses = []

        for expense in self.expenses:
            if expense.category == category:
                filtered_expenses.append(expense)

        return filtered_expenses


    def calculate_summary(self, expenses):
        return sum(e.amount for e in expenses)