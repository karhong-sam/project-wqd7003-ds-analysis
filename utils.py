from datetime import datetime
from dateutil.relativedelta import relativedelta

# functions
def bold(text):
    """This function return text with bold

    Args:
        text (str): normal text to bold

    Returns:
        str: A bold text
    """
    return f"**{text}**"

def calculate_age(dob):
    """
    Calculate age based on date of birth.

    Args:
        dob (str): Date of birth in format "YYYY-MM-DD"

    Returns:
        int: Age in years
    """
    today = datetime.now().date()
    dob = datetime.strptime(dob, "%Y-%m-%d").date()
    age = relativedelta(today, dob).years
    return age