# User handling
import json
import os
# Ranks
ranks = {
    "new user": "New User",
    "guest":    "Guest",
    "premium":  "Premium",
    "employee": "Employee",
    "admin":    "Admin",
}

# Register account
def register(username, password, users_list, user_class, rank_enum):
    """
    users_list
    user_class
    rank_enum
    """
    if not username or not password:
        return False, "Please enter both username and password." 
    if any(u.username == username for u in users_list):
        return False, "Username already exists. Try again."
    new_user = user_class(
        username=username, 
        password=password, 
        rank=rank_enum.new_user, 
        bookings=[]
    )
    
    return True, new_user

# Login account
def login(username, password, users_list):
    if not username or not password:
        return False, None, "Please enter both username and password."
    
    for user in users_list:
        if user.username == username:
            if user.password == password:
                return True, user, f"Login successful - {user.rank.value}"
            else:
                return False, None, "Incorrect password. Please try again."
    
    return False, None, "Username not found. Please register and login your account."

# User information
def get_user_information(user_obj):
    if not user_obj:
        return None 
    
    return {
        "username": user_obj.username,
        "rank": user_obj.rank.value,
        "rank_display": ranks.get(user_obj.rank.value, user_obj.rank.value),
        "bookings_count": len(user_obj.bookings)

    }
