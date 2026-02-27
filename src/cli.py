from expense_tracker.services.expense_service import ExpenseService
from expense_tracker.utils.formatter import print_expenses
from expense_tracker.utils.validation import validate_date, validate_amount

def handle_add(service):
    amount_text = input("Amount (EUR): ")
    amount = validate_amount(amount_text)

    date_text = input("Date (YYYY-MM-DD): ")
    dt = validate_date(date_text)

    category = input("Category: ")
    description = input("Description: ")

    service.add_expense(amount, dt, category, description)
    print("Expense succesfully added.\n")

def handle_view(service):
    expenses = service.get_expenses()
    if not expenses:
        print(f"\nNo expenses recorded yet.\n")
    print_expenses(expenses)

def handle_filter(service):
    category = input("Category to filter: ")

    filtered = service.filter_expenses(category)
    if not filtered:
        print(f"\nNo expenses recorded yet.\n")
    print_expenses(filtered)

def handle_summary(service):
    category = input("Choose a category to filter on: ")

    filtered = service.filter_expenses(category)
    total = service.calculate_summary(filtered)

    print(f"\nTotal spent on {category}: {total} EUR.\n")

commands = {
    'add': handle_add,
    'view': handle_view,
    'filter': handle_filter,
    'summary': handle_summary
}


def main():

    print("Expense tracker running.")

    service = ExpenseService()

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
                handle_add(service)
            case "view":
                handle_view(service)
            case "filter":
                handle_filter(service)
            case "summary":
                handle_summary(service)
            case "quit":
                return


if __name__ == '__main__':
    main()