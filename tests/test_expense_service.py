import pytest 

from expense_tracker.services.expense_service import ExpenseService
from fake_storage import FakeStorage

@pytest.fixture
def expense_service():
    return ExpenseService(FakeStorage())

def test_get_expenses_initially_empty(expense_service):
    assert expense_service.get_expenses() == []

def test_add_expense(expense_service):
    assert expense_service.get_expenses() == []

    expense_service.add_expense(75, '2025-04-22', 'Entertainment', 'Restaurant')

    assert len(expense_service.get_expenses()) == 1

def test_add_multiple_expenses(expense_service):
    assert expense_service.get_expenses() == []

    expense_service.add_expense(75, '2025-04-22', 'Entertainment', 'Restaurant')
    expense_service.add_expense(150, '2026-01-15', 'Groceries', 'Food')
    expense_service.add_expense(40, '2025-08-31', 'Insurance', 'Car insurance')

    assert len(expense_service.get_expenses()) == 3

def test_filter_expenses(expense_service):
    assert expense_service.get_expenses() == []

    expense_service.add_expense(75, '2025-04-22', 'Entertainment', 'Restaurant')
    expense_service.add_expense(150, '2026-01-15', 'Entertainment', 'Cinema')
    expense_service.add_expense(40, '2025-08-31', 'Insurance', 'Car insurance')

    assert len(expense_service.filter_expenses('Entertainment')) == 2
    assert len(expense_service.filter_expenses('Insurance')) == 1
    assert len(expense_service.filter_expenses('Groceries')) == 0

def test_calculate_summary(expense_service):
    assert expense_service.calculate_summary(expense_service.get_expenses()) == 0

    expense_service.add_expense(75, '2025-04-22', 'Entertainment', 'Restaurant')
    expense_service.add_expense(150, '2026-01-15', 'Entertainment', 'Cinema')
    expense_service.add_expense(40, '2025-08-31', 'Insurance', 'Car insurance')

    assert expense_service.calculate_summary(expense_service.get_expenses()) == 265
