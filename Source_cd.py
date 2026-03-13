#=#=#IMPORTANT#=#=#
#DOWNLOAD THESE BEFORE YOU START CODING OR EXECUTING THE CODE
#NOTE: requires customtkinter module (python -m pip install customtkinter)
#NOTE: requires tkinter (usually included with python but if missing install using "python -m pip install tk")

from user_handling import register, login
from booking_handling import create_booking
import movie_handling

find_movie = movie_handling.find_movie
add_movie = movie_handling.add_movie
remove_movie = movie_handling.remove_movie
update_movie = movie_handling.update_movie
list_movies = movie_handling.list_movies

def register_user(username, password, users_list, user_class, rank_enum):

    success, result = register(username, password, users_list, user_class, rank_enum)

    if success:
        users_list.append(result)

    return success, result


def login_user(username, password, users_list):

    return login(username, password, users_list)


def book_ticket(user, movie_title, seats):
    success, msg = movie_handling.book_ticket(movie_title, seats)
    if success:
        movie = find_movie(movie_title)
        premiere_date = movie.get("premiere_date", "") if movie else ""
        create_booking(user, movie_title, seats, premiere_date)
    return success, msg


def admin_add_movie(title, seats, showtime="", premiere_date=""):
    return add_movie(title, seats, showtime, premiere_date)


def admin_remove_movie(title):
    return remove_movie(title)


def admin_update_movie(title, seats=None, showtime=None, premiere_date=None):
    return update_movie(title, seats, showtime, premiere_date)


def admin_list_movies():
    return list_movies()