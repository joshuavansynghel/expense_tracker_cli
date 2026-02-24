from models.expense import Expense

class FakeStorage:

    def __init__(self):
        self.expenses = []

    def _create_mock_data(self):
        expenses = []

        expenses.append(Expense(150, '2025-05-01', 'Entertainment', 'Playstation subscription'))
        expenses.append(Expense(98, '2025-04-30', 'Entertainment', 'DataCamp subscription'))
        expenses.append(Expense(63, '2025-03-14', 'Groceries', 'Food'))

        return expenses

    def store_expenses(self, expenses):
        self.expenses = expenses

    def load_expenses(self):
        return self.expenses