#=#=#IMPORTANT#=#=#
#DOWNLOAD THESE BEFORE YOU START CODING OR EXECUTING THE CODE
#NOTE: requires customtkinter module (python -m pip install customtkinter)
#NOTE: requires tkinter (usually included with python but if missing install using "python -m pip install tk")

from user_handling import register, login
from booking_handling import create_booking
from movie_handling import find_movie

def register_user(username, password, users_list, user_class, rank_enum):

    success, result = register(username, password, users_list, user_class, rank_enum)

    if success:
        users_list.append(result)

    return success, result


def login_user(username, password, users_list):

    return login(username, password, users_list)


def book_ticket(user, movie_title, seats):

    movie = find_movie(movie_title)

    if not movie:
        return False, "Movie not found"

    if movie["seats"] < seats:
        return False, "Not enough seats"

    movie["seats"] -= seats

    create_booking(user, movie_title, seats)

    return True, "Booking successful"
