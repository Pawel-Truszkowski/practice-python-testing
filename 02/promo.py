import string

def is_valid_promo(code):
    if not isinstance(code, str):
        return False
    if len(code) < 10 or len(code) > 10:
        return False
    if any(char.islower() for char in code):
        return False
    if len([char for char in code if char.isdigit()]) < 2:
        return False
    if not code.isalnum():
        return False
    
    return True

