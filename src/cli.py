import sys

from expense_tracker.services.expense_service import ExpenseService
from expense_tracker.utils.formatter import print_expenses
from expense_tracker.utils.validation import validate_date, validate_amount, validate_string, validate_id

def prompt_valid_input(prompt, validator):
    while True:
        value = input(prompt)
        try:
            return validator(value)
        except ValueError as e:
            print(e)

def handle_add(service):
    amount = prompt_valid_input(
        "Amount (EUR): ",
        validate_amount
    )

    dt = prompt_valid_input(
        "Date (YYYY-MM-DD): ",
        validate_date
    )

    category = prompt_valid_input(
        "Category: ",
        validate_string
    )

    description = prompt_valid_input(
        "Description: ",
        validate_string
    )

    service.add_expense(amount, dt, category, description)
    print("Expense successfully added.")

def handle_delete(service):
    id = prompt_valid_input(
        "ID: ",
        validate_id
    )

    service.delete_expense(id)
    print("Expense successfully deleted.")

def handle_view(service):
    expenses = service.get_expenses()
    if not expenses:
        print(f"\nNo expenses recorded yet.")
        return
    print_expenses(expenses)

def handle_filter(service):
    category = prompt_valid_input(
        "Category to filter: ",
        validate_string
    )

    filtered = service.filter_expenses(category)
    if not filtered:
        print(f"\nNo expenses recorded yet for the category '{category}' yet.")
    else:
        print_expenses(filtered)

def handle_summary(service):
    category = input("Choose a category to filter on: ")

    filtered = service.filter_expenses(category)
    total = service.calculate_summary(filtered)

    print(f"\nTotal spent on {category}: {total} EUR.")

commands = {
    'add': handle_add,
    'delete': handle_delete,
    'view': handle_view,
    'filter': handle_filter,
    'summary': handle_summary,
}


def main():

    print("Expense tracker running.")

    service = ExpenseService()

    while True:
        print("\nWhat would you like to do?\n")
        choice = input(
            "Type 'add' to add an expense\n"
            "Type 'delete' to delete an expense\n"
            "Type 'view' to view all expenses\n"
            "Type 'filter' to filter on specific expenses\n"
            "Type 'summary' to generate a summary for a specific category\n"
            "Type 'quit' to quit the application\n"
        ).strip().lower()

        if choice == 'quit':
            sys.exit(0)

        try:
            handler = commands.get(choice)
            handler(service)
        except ValueError:
            print(f"'{choice}' is not a valid command.")


if __name__ == '__main__':
    main()