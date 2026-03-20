from expense_tracker.models.expense import Expense
from expense_tracker.storage.expense_storage import ExpenseStorage
from expense_tracker.config.settings import EXPENSES_PATH


class ExpenseService:

    def __init__(self, expense_storage=None):
        self.expense_storage = expense_storage or ExpenseStorage(EXPENSES_PATH)
        self.expenses = self.expense_storage.load_expenses()

    
    def find_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None


    def get_expenses(self):
        return self.expenses.copy()
    

    def get_categories(self):
        return sorted(list({e.category for e in self.expenses}), key=str.lower)
    
    def _save(self):
        self.expense_storage.store_expenses(self.expenses)


    def add_expense(self, amount, date, category, description):
    
        # Instantiate expense
        expense = Expense(amount, date, category, description)

        # Store locally and persistent
        self.expenses.append(expense)
        self._save()

    
    def edit_expense(self, expense_id, amount, date, category, description):
        expense = self.find_expense(expense_id)

        if expense:
            expense.amount = amount
            expense.date = date
            expense.category = category
            expense.description = description

            self._save()

            return expense
        else:
            return None

    
    def delete_expense(self, expense_id):
        expense = self.find_expense(expense_id)
        if expense:
            self.expenses.remove(expense)
            self._save()
            return expense
        else:
            return None


    def filter_expenses(self, category):
        return [e for e in self.expenses if e.category == category]


    def calculate_summary(self, expenses):
        return sum(e.amount for e in expenses)