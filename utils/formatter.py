def print_expenses(expenses):
    print("DATE \t AMOUNT \T CATEGORY \t DESCRIPTION")

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: (-expense.date, expense.category)
    )

    for expense in sorted_expenses:
        print(expense)