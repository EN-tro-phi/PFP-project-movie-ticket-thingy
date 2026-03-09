import json
import os
from models import User, RankEnum

USERS_FILE = "users.json"

def save_users(users_list):

    data = []

    for user in users_list:
        data.append({
            "username": user.username,
            "password": user.password,
            "rank": user.rank.value,
            "bookings": user.bookings
        })

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


MOVIES_FILE = "movies.json"

def save_movies(movies_list):

    data = []

    for m in movies_list:
        data.append({
            "title": m.get("title"),
            "seats": m.get("seats"),
            "showtime": m.get("showtime", ""),
            "premiere_date": m.get("premiere_date", "")
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
            "premiere_date": m.get("premiere_date", "")
        }
        movies_list.append(movie)

    return movies_list
