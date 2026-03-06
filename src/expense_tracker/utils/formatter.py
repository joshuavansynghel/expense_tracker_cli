def print_expenses(expenses):
    # Format header
    print(f"{'ID':<5} | {'DATE':<12} | {'AMOUNT':>10} | {'CATEGORY':<15} | DESCRIPTION")
    print("-" * 75)

    # Sort on dates descending and category ascending
    sorted_expenses = sorted(
        expenses,
        key=lambda expense: (expense.date, expense.category),
        reverse=True
    )

    # Print expenses
    for expense in sorted_expenses:
        print(
            f"{expense.id:<5} | "
            f"{expense.date.strftime('%Y-%m-%d'):<12} | "
            f"EUR{expense.amount:>7.2f} | "
            f"{expense.category:<15} | "
            f"{expense.description}"
        )