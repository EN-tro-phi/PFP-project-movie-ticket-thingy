# User handling
import json
import os
from enum import Enum

# Ranks
class Rank(Enum):
    NEW_USER = "new user"
    GUEST = "guest"
    PREMIUM = "premium"
    EMPLOYEE = "employee"
    ADMIN = "admin"

ranks = {
    "new user": "New User",
    "guest":    "Guest",
    "premium":  "Premium",
    "employee": "Employee",
    "admin":    "Admin",
}

class User:
    def __init__(self, username, password, rank, bookings=None):
        self.username = username
        self.password = password
        self.rank = rank
        self.bookings = bookings or []

def load_users():
    file_path = "users.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            users = []
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 3:
                    username = parts[0]
                    password = parts[1]
                    rank_str = parts[2]
                    bookings_str = parts[3] if len(parts) > 3 else "[]"
                    try:
                        rank = Rank(rank_str)
                        bookings = json.loads(bookings_str)
                    except (ValueError, json.JSONDecodeError):
                        continue  # Skip invalid lines
                    users.append(User(username, password, rank, bookings))
            return users
    return []

def save_users(users):
    file_path = "users.txt"
    with open(file_path, "w") as f:
        for user in users:
            bookings_str = json.dumps(user.bookings)
            f.write(f"{user.username}|{user.password}|{user.rank.value}|{bookings_str}\n")

# Create user (register)
def create_user(username, password):
    """
    Creates a new user and saves to file.
    """
    if not username or not password:
        return False, "Please enter both username and password."
    users = load_users()
    if any(u.username == username for u in users):
        return False, "Username already exists. Try again."
    new_user = User(
        username=username, 
        password=password, 
        rank=Rank.NEW_USER, 
        bookings=[]
    )
    users.append(new_user)
    save_users(users)
    return True, new_user

# Login user
def login_user(username, password):
    if not username or not password:
        return False, None, "Please enter both username and password."
    
    users = load_users()
    for user in users:
        if user.username == username:
            if user.password == password:
                return True, user, f"Login successful - Welcome, {ranks.get(user.rank.value, user.rank.value)}!"
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