def print_expenses(expenses):
    # Check if expenses is not empty
    if not expenses:
        print("No expenses have been added yet")
        return

    # Format header
    print("DATE \t| AMOUNT \t| CATEGORY \t| DESCRIPTION")

    # Sort on dates descending and category ascending
    sorted_expenses = sorted(
        expenses,
        key=lambda expense: (-expense.date, expense.category)
    )

    # Print expenses
    for expense in sorted_expenses:
        print(f"{expense.date}\t| {expense.amount}\t| \
              {expense.category}\t| {expense.description}")