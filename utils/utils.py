def find_user(user_email, user_col):
    user = user_col.find_one({'email': user_email})
    if user:
        return user
    return None

def list_products():
    return