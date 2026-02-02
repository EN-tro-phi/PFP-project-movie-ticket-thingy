#=#=#IMPORTANT#=#=#
#DOWNLOAD THESE BEFORE YOU START CODING OR EXECUTING THE CODE
#NOTE: requires customtkinter module (python -m pip install customtkinter)
#NOTE: requires tkinter (usually included with python but if missing install using "python -m pip install tk")

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

import datetime
import json
import os

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict


class Rank(Enum):
    NEW_USER = "new user"
    GUEST = "guest"
    PREMIUM = "premium"
    EMPLOYEE = "employee"
    ADMIN = "admin"

RANK_COLORS = {
    Rank.NEW_USER: "gray",
    Rank.GUEST: "green",
    Rank.PREMIUM: "goldenrod",
    Rank.EMPLOYEE: "blue",
    Rank.ADMIN: "red"
}

User_filepath = "users.json"
Movie_filepath = "movies.json"


@dataclass
class User:
    username: str
    password: str
    rank: Rank = Rank.NEW_USER
    bookings: List[Dict] = field(default_factory=list)
    


def user_to_dict(user: User) -> Dict:
    return {
        "username": user.username,
        "password": user.password,
        "rank": user.rank.value,
    }
def dict_to_user(data: Dict) -> User:
    return User(
        username=data["username"],
        password=data.get("password", data.get("password_hash", "")),
        rank=Rank(data.get("rank", Rank.NEW_USER.value)),
        bookings=data.get("bookings", [])
    )
    
def load_users() -> List[User]:
    if not User_filepath or not os.path.exists(User_filepath):
        return []
    
    with open(User_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [dict_to_user(u) for u in data]
    
def save_users(users: List[User]):
    with open(User_filepath, "w", encoding="utf-8") as f:
        data = [user_to_dict(u) for u in users]
        json.dump(data, f, indent=4)
        
def create_user(username: str, password: str, rank: Rank = Rank.NEW_USER) -> User:
    return User(username=username, password=password, rank=rank)

def user_login(username: str, password: str) -> User:
    users = load_users()
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None        

#This part is for ADMIN and EMPLOYEE ONLY 
def load_movies() -> List[Dict]:
    if not Movie_filepath or not os.path.exists(Movie_filepath):
        return []
    
    with open(Movie_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

    
def save_movies(movies: List[Dict]):
    with open(Movie_filepath, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)