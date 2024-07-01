"""
These are common validator functions that can be used by any module.
Validator function has only one task - validate data.
"""


def is_phone_number_valid(phone: str) -> bool:
    """
    Return if phone number is valid or not
    """
    try:
        phone = int(phone)
    except ValueError:
        return False
    if phone < 1000000000 or phone > 9999999999:
        return False
    return True
