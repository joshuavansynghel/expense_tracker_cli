import pytest 

from expense_tracker.services.expense_service import ExpenseService
from expense_tracker.models.expense import Expense
from fake_storage import FakeStorage

@pytest.fixture
def expense_service():
    return ExpenseService(FakeStorage())

def test_get_expenses_initially_empty(expense_service):
    assert expense_service.get_expenses() == []

def test_add_expense(expense_service):
    expense_service.add_expense(75, '2025-04-22', 'Entertainment', 'Restaurant')

    assert len(expense_service.get_expenses()) == 1

