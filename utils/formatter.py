def print_expenses(expenses):
    # Check if expenses is not empty
    if not expenses:
        print("No expenses have been added yet")
        return

    # Format header
    print(f"{'DATE':<12} | {'AMOUNT':>10} | {'CATEGORY':<15} | DESCRIPTION")
    print("-" * 65)

    # Sort on dates descending and category ascending
    sorted_expenses = sorted(
        expenses,
        key=lambda expense: (expense.date, expense.category),
        reverse=True
    )

    # Print expenses
    for expense in sorted_expenses:
        print(
            f"{expense.date.strftime('%Y-%m-%d'):<12} | "
            f"€{expense.amount:>10.2} | "
            f"{expense.category:<15} | "
            f"{expense.description}"
        )