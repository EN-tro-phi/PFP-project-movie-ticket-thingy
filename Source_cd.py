#=#=#IMPORTANT#=#=#
#DOWNLOAD THESE BEFORE YOU START CODING OR EXECUTING THE CODE
#NOTE: requires customtkinter module (python -m pip install customtkinter)
#NOTE: requires tkinter (usually included with python but if missing install using "python -m pip install tk")

from user_handler import create_user, login_user
from booking_handler import create_booking


def register(username, password):
    return create_user(username, password)


def login(username, password):
    return login_user(username, password)


def book_ticket(username, movie, seats):
    create_booking(username, movie, seats)
