from models.expense import Expense

def main():

    print("Expense tracker running.")

    test_expense = Expense(5, '2025-01-05', 'Groceries', 'Colruyt')

    print(test_expense)
    print(f"Purchased {test_expense.description} for €{test_expense.amount} on {test_expense.date}")

def add_expense():
    amount_text = input("")


if __name__ == '__main__':
    main()