from models.expense import Expense
from utils.validation import validate_date, validate_amount

def add_expense():
    # Amount input
    amount_text = input("What is the amount of the expense in euros?: ")
    amount = validate_amount(amount_text)

    date_text = input("What is the date of the expense?: ")
    dt = validate_date(date_text)

    category_text = input("What is the category of the expense?: ")
    description_text = input("What is the description of the expense?: ")

    return Expense(amount, dt, category_text, description_text)


def filter_expenses(expenses, category):
    filtered_expenses = []

    for expense in expenses:
        if expense.category == category:
            filtered_expenses.append(expense)

    return filtered_expenses

def calculate_summary(expenses):
    return sum(e.amount for e in expenses)