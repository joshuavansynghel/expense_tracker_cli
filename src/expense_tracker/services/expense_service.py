from expense_tracker.models.expense import Expense
from expense_tracker.storage.expense_storage import ExpenseStorage
from expense_tracker.config.settings import EXPENSES_PATH


class ExpenseService:

    def __init__(self, expense_storage=None):
        self.expense_storage = expense_storage or ExpenseStorage(EXPENSES_PATH)
        self.expenses = self.expense_storage.load_expenses()

    
    def find_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                return expense
        return None


    def get_expenses(self):
        return self.expenses
    

    def add_expense(self, amount, date, category, description):
    
        # Instantiate expense
        expense = Expense(amount, date, category, description)

        # Store locally and persistent
        self.expenses.append(expense)
        self.expense_storage.store_expenses(self.expenses)

    
    def edit_expense(self, id, amount, date, category, description):
        expense = self.find_expense(id)
        if expense is None:
            return False
        else:
            expense.amount = amount
            expense.date = date
            expense.category = category
            expense.description = description

            self.expense_storage.store_expenses(self.expenses)

    
    def delete_expense(self, id):
        expense = self.find_expense(id)
        if expense is None:
            return False
        else:
            self.expenses.remove(expense)


    def filter_expenses(self, category):
        filtered_expenses = []

        for expense in self.expenses:
            if expense.category == category:
                filtered_expenses.append(expense)

        return filtered_expenses


    def calculate_summary(self, expenses):
        return sum(e.amount for e in expenses)