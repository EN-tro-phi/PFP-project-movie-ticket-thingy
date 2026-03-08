import json
import os

def load_users(file_path, user_class, rank_enum):

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        data = json.load(f)

    users = []

    for u in data:
        users.append(
            user_class(
                username=u["username"],
                password=u["password"],
                rank=rank_enum[u["rank"]],
                bookings=u.get("bookings", [])
            )
        )

    return users


def save_users(file_path, users_list):

    data = []

    for user in users_list:
        data.append({
            "username": user.username,
            "password": user.password,
            "rank": user.rank.name,
            "bookings": user.bookings
        })

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
