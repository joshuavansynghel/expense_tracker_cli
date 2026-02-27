from datetime import datetime, date

def validate_date(date_text):
    try:
        return date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    
def validate_amount(amount_text):
    try:
        amount = float(amount_text)
        return amount
    except ValueError:
        raise ValueError("Incorrect amount format, should be a positive number")
    
