from datetime import datetime

def validate_date(date_text):
    try:
        dt = datetime.strptime(date_text, '%Y-%m-%d')
        return dt
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    
def validate_amount(amount_text):
    try:
        amount = float(amount_text)
        return amount
    except ValueError:
        raise ValueError("Incorrect amount format, should be a positive number")
    
