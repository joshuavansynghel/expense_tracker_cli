from services.expense_service import add_expense, filter_expenses, calculate_summary
from utils.formatter import print_expenses

def main():

    print("Expense tracker running.")

    expenses = []

    while True:
        print("\nWhat would you like to do?\n")
        choice = input(
            "Type 'add' to add an expense\n"
            "Type 'view' to view allexpenses\n"
            "Type 'filter' to filter on specific expenses\n"
            "Type 'summary' to generate a summary for a specific category\n"
            "Type 'quit' to quit the application\n"
        )

        match choice:
            case "add":
                expenses.append(add_expense())

            case "view":
                print_expenses(expenses)

            case "filter":
                category_choice = input("Choose a category to filter on: ")
                filtered_expenses = filter_expenses(expenses,category_choice)
                print_expenses(filtered_expenses)

            case "summary":
                category_choice = input("Choose a category to filter on: ")
                filtered_expenses = filter_expenses(expenses,category_choice)
                total = calculate_summary(filtered_expenses)
                print(f"You've spent a total of €{total} on {category_choice}.")
            case "quit":
                return


if __name__ == '__main__':
    main()