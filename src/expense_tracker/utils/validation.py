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
    
def validate_id(id_text):
    try:
        id = int(id_text)
        return id
    except ValueError:
        raise ValueError("Incorrect ID format, should be a positive whole number")
    
def validate_string(string):
    if not isinstance(string, str):
        raise ValueError("String expected")
    return string.strip().title()
    
