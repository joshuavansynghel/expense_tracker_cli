from models.expense import Expense
from utils.validation import validate_date, validate_amount

def main():

    print("Expense tracker running.")

    expenses = []

    while True:
        expenses.append(add_expense())
        finished_flag = input("Want to add another expense? (Y/N)")
        if finished_flag == 'N':
            break

    for expense in expenses:
        print(expense)



def add_expense():
    # Amount input
    amount_text = input("What is the amount of the expense in euros?: ")
    amount = validate_amount(amount_text)

    date_text = input("What is the date of the expense?: ")
    dt = validate_date(date_text)

    category_text = input("What is the category of the expense?: ")
    description_text = input("What is the description of the expense?: ")

    return Expense(amount, dt, category_text, description_text)



if __name__ == '__main__':
    main()