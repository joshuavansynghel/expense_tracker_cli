from datetime import datetime

def validate_date(date_text):
    try:
        datetime.time.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    
def validate_amount(amount_text):
    try:
        amount = int(amount_text)
        return amount > 0
    except ValueError:
        raise ValueError("Incorrect amount format, should be a positive number")
    
