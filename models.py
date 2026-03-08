from enum import Enum

class RankEnum(Enum):
    new_user = "new user"
    guest = "guest"
    premium = "premium"
    employee = "employee"
    admin = "admin"


class User:
    def __init__(self, username, password, rank, bookings=None):
        self.username = username
        self.password = password
        self.rank = rank
        self.bookings = bookings if bookings else []
