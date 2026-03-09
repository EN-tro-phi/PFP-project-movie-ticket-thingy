from models import User, RankEnum

def register(username, password, users_list, user_class, rank_enum):
    if username == "" or password == "":
        return False, "Please enter username and password."
    for user in users_list:
        if user.username == username:
            return False, "Username already exists."
    new_user = user_class(
        username=username,
        password=password,
        rank=rank_enum.new_user,
        bookings=[]
    )
    return True, new_user

def login(username, password, users_list):
    if username == "" or password == "":
        return False, None
    for user in users_list:
        if user.username == username and user.password == password:
            return True, user
    return False, None

def get_user_information(user):
    if user is None:
        return None
    return {
        "username": user.username,
        "rank": user.rank.name,
        "bookings_count": len(user.bookings)
    }

