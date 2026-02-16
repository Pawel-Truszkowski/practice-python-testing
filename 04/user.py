def validate_user(data):
    char = "@"
    if char not in data['email']:
        return False
    
    if not data['email'].endswith((".pl", ".com")):
        return False
    
    if isinstance(data['age'], int) and data['age'] < 18:
        return False
        
    if not data['name'].isalpha():
        return False
    
    return True

