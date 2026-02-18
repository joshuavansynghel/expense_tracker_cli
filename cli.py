from models.expense import Expense
from utils.validation import validate_date, validate_amount
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
            case "quit":
                return
            


def add_expense():
    # Amount input
    amount_text = input("What is the amount of the expense in euros?: ")
    amount = validate_amount(amount_text)

    date_text = input("What is the date of the expense?: ")
    dt = validate_date(date_text)

    category_text = input("What is the category of the expense?: ")
    description_text = input("What is the description of the expense?: ")

    return Expense(amount, dt, category_text, description_text)


def filter_expenses(expenses, category):
    filtered_expenses = []

    for expense in expenses:
        if expense.category == category:
            filtered_expenses.append(expense)

    return filtered_expenses



if __name__ == '__main__':
    main()