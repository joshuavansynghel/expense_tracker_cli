from expense_tracker.services.expense_service import ExpenseService
from expense_tracker.utils.formatter import print_expenses
from expense_tracker.utils.validation import validate_date, validate_amount


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
                # Ask user for input and validate 
                amount_text = input("What is the amount of the expense in euros?: ")
                amount = validate_amount(amount_text)

                date_text = input("What is the date of the expense?: ")
                dt = validate_date(date_text)

                category_text = input("What is the category of the expense?: ")
                description_text = input("What is the description of the expense?: ")

                expense_service.add_expense(amount, dt, category_text, description_text)

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