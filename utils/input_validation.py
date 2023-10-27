import re

def password_validation(password):
    pattern = '^[(a-zA-Z0-9)]{12,20}$'
    answer = re.match(pattern,password)
    if answer is not None:
        return True
    else:
        return False
    