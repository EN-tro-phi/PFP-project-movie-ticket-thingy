#Extra code, dont mind.
import tkinter as tk
from tkinter import messagebox
from source_cd import register_user, login_user_system, book_movie
current_user = None
def register():
    username = entry_username.get()
    password = entry_password.get()
    if username == "" or password == "":
        messagebox.showerror("Error", "Enter username and password")
        return
    success = register_user(username, password)
    if success:
        messagebox.showinfo("Success", "User registered")
    else:
        messagebox.showerror("Error", "Username already exists")
def login():
    global current_user
    username = entry_username.get()
    password = entry_password.get()
    success = login_user_system(username, password)
    if success:
        current_user = username
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid login")
def book_ticket():
    if current_user is None:
        messagebox.showerror("Error", "Please login first")
        return
    movie = entry_movie.get()
    seats = entry_seats.get()
    if movie == "" or seats == "":
        messagebox.showerror("Error", "Enter movie and seats")
        return
    if not seats.isdigit():
        messagebox.showerror("Error", "Seats must be a number")
        return
    book_movie(current_user, movie, int(seats))
    messagebox.showinfo("Success", "Booking confirmed")
def start_ui():
    global entry_username, entry_password, entry_movie, entry_seats
    root = tk.Tk()
    root.title("Movie Ticket System")
    root.geometry("300x300")
    
    tk.Label(root, text="Username").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Register", command=register).pack(pady=5)
    tk.Button(root, text="Login", command=login).pack(pady=5)

    tk.Label(root, text="Movie Name").pack()
    entry_movie = tk.Entry(root)
    entry_movie.pack()

    tk.Label(root, text="Seats").pack()
    entry_seats = tk.Entry(root)
    entry_seats.pack()

    tk.Button(root, text="Book Ticket", command=book_ticket).pack(pady=10)

    root.mainloop()
start_ui()
