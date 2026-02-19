from services.expense_service import ExpenseService
from utils.formatter import print_expenses

def main():

    print("Expense tracker running.")

    expense_service = ExpenseService()

    while True:
        print("\nWhat would you like to do?\n")
        choice = input(
            "Type 'add' to add an expense\n"
            "Type 'view' to view all expenses\n"
            "Type 'filter' to filter on specific expenses\n"
            "Type 'summary' to generate a summary for a specific category\n"
            "Type 'quit' to quit the application\n"
        )

        match choice:
            case "add":
                expense_service.add_expense()

            case "view":
                print_expenses(expense_service.get_expenses())

            case "filter":
                category_choice = input("Choose a category to filter on: ")

                filtered_expenses = expense_service.filter_expenses(category_choice)
                print_expenses(filtered_expenses)

            case "summary":
                category_choice = input("Choose a category to filter on: ")

                filtered_expenses = expense_service.filter_expenses(category_choice)
                total = expense_service.calculate_summary(filtered_expenses)
                
                print(f"You've spent a total of €{total} on {category_choice}.")
            case "quit":
                return


if __name__ == '__main__':
    main()