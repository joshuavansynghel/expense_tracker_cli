import pytest 

from models.expense import Expense
from services.expense_service import ExpenseService
from fake_storage import FakeStorage

@pytest.fixture
def expense_service():
    return ExpenseService(FakeStorage())

def test_get_expenses_initially_empty(expense_service):
    assert expense_service.get_expenses() == []
