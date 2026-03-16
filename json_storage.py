import json
import os
from models import User, RankEnum

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

def save_users(users_list):

    data = []

    for user in users_list:
        data.append({
            "username": user.username,
            "password": user.password,
            "rank": user.rank.value,
            "bookings": user.bookings
        })

    # if file already exists and contents are identical, don't rewrite
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r") as f:
                existing = json.load(f)
            if existing == data:
                return
        except json.JSONDecodeError:
            # corrupted file, we'll overwrite below
            pass

    # if file already exists and contents are identical, don't rewrite
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r") as f:
                existing = json.load(f)
            if existing == data:
                return
        except json.JSONDecodeError:
            # corrupted file, we'll overwrite below
            pass

    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_users():

    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    users_list = []

    for u in data:
        user = User(
            username=u["username"],
            password=u["password"],
            rank=RankEnum(u["rank"]),
            bookings=u.get("bookings", [])
        )

        users_list.append(user)

    return users_list


def save_user_bookings(users_list):
    save_users(users_list)


def add_user(user):
    """Add a single new user to the JSON file without rewriting everything"""
    users_list = load_users()
    users_list.append(user)
    save_users(users_list)


MOVIES_FILE = os.path.join(BASE_DIR, "movies.json")

def save_movies(movies_list):

    data = []

    for m in movies_list:
        data.append({
            "title": m.get("title"),
            "seats": m.get("seats"),
            "showtime": m.get("showtime", ""),
            "premiere_date": m.get("premiere_date", ""),
            # persist per-seat bookings if present
            "booked_seats": m.get("booked_seats", [])
        })

    with open(MOVIES_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_movies():

    if not os.path.exists(MOVIES_FILE):
        return []

    with open(MOVIES_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    movies_list = []

    for m in data:
        movie = {
            "title": m.get("title"),
            "seats": m.get("seats"),
            "showtime": m.get("showtime", ""),
            "premiere_date": m.get("premiere_date", ""),
            # load any stored per-seat bookings; default to empty list
            "booked_seats": m.get("booked_seats", [])
        }
        movies_list.append(movie)

    return movies_list
