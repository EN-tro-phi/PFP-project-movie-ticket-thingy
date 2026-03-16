import tkinter as tk
from tkinter import messagebox

from Source_cd import register_user, login_user, book_ticket as book_ticket_func, \
    admin_add_movie, admin_remove_movie, admin_update_movie, admin_list_movies
from json_storage import load_users, save_users
from models import User, RankEnum

users_list = load_users()

admin_frame = None
entry_admin_title = None
entry_admin_seats = None
entry_admin_showtime = None
entry_admin_premiere_date = None
text_movie_list = None

entry_username = None
entry_password = None
register_button = None
login_button = None
label_status = None

from Source_cd import register_user, login_user, book_ticket as book_ticket_func, \
    admin_add_movie, admin_remove_movie, admin_update_movie, admin_list_movies
from json_storage import load_users, save_users
from models import User, RankEnum

users_list = load_users()

admin_frame = None
entry_admin_title = None
entry_admin_seats = None
entry_admin_showtime = None
entry_admin_premiere_date = None
text_movie_list = None

entry_username = None
entry_password = None
register_button = None
login_button = None
label_status = None


current_user = None

def register():
    username = entry_username.get()
    password = entry_password.get()

    chosen_rank = RankEnum.admin if len(users_list) == 0 else RankEnum.new_user

    success, result = register_user(username, password, users_list, User, chosen_rank)
    chosen_rank = RankEnum.admin if len(users_list) == 0 else RankEnum.new_user

    success, result = register_user(username, password, users_list, User, chosen_rank)

    if success:
        # newly created user object is in 'result'
        # add just that user to storage; this avoids rewriting the file multiple times and
        # ensures the JSON is created only once during the life of the program.
        from json_storage import add_user
        add_user(result)
        users_list.append(result)  # keep the in-memory list in sync
        # newly created user object is in 'result'
        # add just that user to storage; this avoids rewriting the file multiple times and
        # ensures the JSON is created only once during the life of the program.
        from json_storage import add_user
        add_user(result)
        users_list.append(result)  # keep the in-memory list in sync
        messagebox.showinfo("Success", "User registered")
        if chosen_rank == RankEnum.admin:
            messagebox.showinfo("Notice", "First user created; assigned admin rank.")
        if chosen_rank == RankEnum.admin:
            messagebox.showinfo("Notice", "First user created; assigned admin rank.")
    else:
        messagebox.showerror("Error", result)
        messagebox.showerror("Error", result)

def login():
    global current_user

    username = entry_username.get()
    password = entry_password.get()

    success, user = login_user(username, password, users_list)
    success, user = login_user(username, password, users_list)

    if success:
        current_user = user
        current_user = user
        messagebox.showinfo("Success", "Login successful")
        if label_status:
            label_status.config(text=f"Logged in as {current_user.username}")
        if register_button:
            register_button.config(state=tk.DISABLED)
        if login_button:
            login_button.config(state=tk.DISABLED)
        entry_username.config(state=tk.DISABLED)
        entry_password.config(state=tk.DISABLED)

        # show or hide admin panel depending on rank
        if hasattr(current_user, 'rank') and current_user.rank == RankEnum.admin:
            admin_frame.pack(pady=10)
            refresh_movie_list()
        else:
            if admin_frame:
                admin_frame.pack_forget()
            messagebox.showinfo("Note", "You are not an admin; admin panel unavailable.")
        if label_status:
            label_status.config(text=f"Logged in as {current_user.username}")
        if register_button:
            register_button.config(state=tk.DISABLED)
        if login_button:
            login_button.config(state=tk.DISABLED)
        entry_username.config(state=tk.DISABLED)
        entry_password.config(state=tk.DISABLED)

        # show or hide admin panel depending on rank
        if hasattr(current_user, 'rank') and current_user.rank == RankEnum.admin:
            admin_frame.pack(pady=10)
            refresh_movie_list()
        else:
            if admin_frame:
                admin_frame.pack_forget()
            messagebox.showinfo("Note", "You are not an admin; admin panel unavailable.")
    else:
        messagebox.showerror("Error", "Invalid login")

def book_ticket_ui():
def book_ticket_ui():
    if current_user is None:
        messagebox.showerror("Error", "Please login first")
        return

    movie = entry_movie.get()
    seats = entry_seats.get()

    if movie == "" or seats == "":
        messagebox.showerror("Error", "Enter movie and seats")
        return

    success, msg = book_ticket_func(current_user, movie, int(seats))
    if success:
        save_users(users_list)
        messagebox.showinfo("Success", msg)
    else:
        messagebox.showerror("Error", msg)


def show_movies():
    """Display available movies in a popup window for logged-in users."""
    if current_user is None:
        messagebox.showerror("Error", "Please login first")
        return

    movies = admin_list_movies()
    if not movies:
        messagebox.showinfo("Movies", "No movies available")
        return

    movie_window = tk.Toplevel()
    movie_window.title("Available Movies")
    movie_window.geometry("400x300")

    tk.Label(movie_window, text="Available Movies", font=("Arial", 12, "bold")).pack(pady=5)

    text_widget = tk.Text(movie_window, height=12, width=50)
    text_widget.pack(pady=5, padx=5)

    for m in movies:
        movie_info = f"Title: {m['title']}\n"
        movie_info += f"Available Seats: {m['seats']}\n"
        movie_info += f"Showtime: {m.get('showtime', 'N/A')}\n"
        movie_info += "-" * 40 + "\n"
        text_widget.insert(tk.END, movie_info)

    text_widget.config(state=tk.DISABLED)

    tk.Button(movie_window, text="Close", command=movie_window.destroy).pack(pady=5)


def show_seat_selection():
    """Open visual seat selection window for booking tickets."""
    if current_user is None:
        messagebox.showerror("Error", "Please login first")
        return

    movie = entry_movie.get()
    if movie == "":
        messagebox.showerror("Error", "Please enter a movie name")
        return

    from movie_handling import find_movie
    movie_data = find_movie(movie)
    if not movie_data:
        messagebox.showerror("Error", "Movie not found")
        return

    seat_window = tk.Toplevel()
    seat_window.title(f"Seat Selection - {movie}")
    seat_window.geometry("600x500")

    tk.Label(seat_window, text=f"Select Seats for {movie}", font=("Arial", 14, "bold")).pack(pady=10)

    canvas = tk.Canvas(seat_window, bg="lightgray", width=550, height=350)
    canvas.pack(pady=10, padx=10)

    canvas.create_rectangle(50, 20, 500, 60, fill="black", outline="black")
    canvas.create_text(275, 40, text="SCREEN", fill="white", font=("Arial", 12, "bold"))

    row_count = 5
    col_count = 8
    seat_width = 40
    seat_height = 30
    start_x = 80
    start_y = 100
    seat_spacing_x = 50
    seat_spacing_y = 40

    # seats currently selected in this UI session
    selected_seats = []
    # map seat_id -> (rect_id, status_dict)
    seat_rects = {}

    # load already-booked seats for this movie from persisted data
    booked_seats_persisted = movie_data.get("booked_seats", [])

    def toggle_seat(row, col):
        """Mark a seat as booked (red) if it is available (blue)."""
        seat_id = f"{row}-{col}"
        rect, seat_status = seat_rects[seat_id]
        # Only allow booking if the seat is currently available in this session
        if seat_status["booked"]:
            return

        seat_status["booked"] = True
        seat_status["selected"] = True
        canvas.itemconfig(rect, fill="red")
        selected_seats.append(seat_id)
        update_seats_label()

    def update_seats_label():
        """Update selected seats label."""
        if selected_seats:
            label_seats.config(text=f"Selected Seats: {len(selected_seats)} ({', '.join(selected_seats)})")
        else:
            label_seats.config(text="Selected Seats: None")

    for row in range(row_count):
        for col in range(col_count):
            x = start_x + col * seat_spacing_x
            y = start_y + row * seat_spacing_y
            seat_id = f"{row}-{col}"

            # determine initial visual state: booked (red) or available (blue)
            initially_booked = seat_id in booked_seats_persisted
            seat_status = {
                "selected": False,
                "booked": initially_booked,
            }
            fill_color = "red" if initially_booked else "blue"
            rect = canvas.create_rectangle(
                x, y, x + seat_width, y + seat_height,
                fill=fill_color, outline="black"
            )
            seat_rects[seat_id] = (rect, seat_status)
            canvas.tag_bind(rect, "<Button-1>", lambda e, r=row, c=col: toggle_seat(r, c))

    label_seats = tk.Label(seat_window, text="Selected Seats: None", font=("Arial", 10))
    label_seats.pack(pady=5)

    confirm_frame = tk.Frame(seat_window)
    confirm_frame.pack(pady=10)

    def confirm_booking():
        """Confirm seat selection and show receipt."""
        if not selected_seats:
            messagebox.showerror("Error", "Please select at least one seat")
            return

        num_seats = len(selected_seats)
        
        receipt_window = tk.Toplevel(seat_window)
        receipt_window.title("Booking Receipt")
        receipt_window.geometry("500x450")
        
        tk.Label(receipt_window, text=" BOOKING RECEIPT", font=("Arial", 16, "bold"), fg="green").pack(pady=15)
        
        receipt_text = tk.Text(receipt_window, height=18, width=60, font=("Courier", 10))
        receipt_text.pack(pady=10, padx=10)
        
        receipt_content = f"""
╔════════════════════════════════════════════════════╗
║           MOVIE TICKET BOOKING RECEIPT             ║
╚════════════════════════════════════════════════════╝

📽️  MOVIE DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Movie Title:        {movie}
  Showtime:           {movie_data.get('showtime', 'N/A')}
  Premiere Date:      {movie_data.get('premiere_date', 'N/A')}

🎫 SEAT INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Number of Seats:    {num_seats}
  Selected Seats:     {', '.join(selected_seats)}

👤 CUSTOMER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Username:           {current_user.username}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Status: ✓ READY TO CONFIRM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        receipt_text.insert(tk.END, receipt_content)
        receipt_text.config(state=tk.DISABLED)
        
        button_frame = tk.Frame(receipt_window)
        button_frame.pack(pady=15)
        
        def finalize_booking():
            """Finalize the booking after confirming receipt."""
            # persist specific seat IDs so they remain booked across sessions
            success, msg = book_ticket_func(current_user, movie, selected_seats.copy())
            if success:
                save_users(users_list)
                messagebox.showinfo("Success", "✓ Booking confirmed and saved!")
                receipt_window.destroy()
                seat_window.destroy()
                show_user_bookings()
            else:
                messagebox.showerror("Error", msg)
        
        tk.Button(button_frame, text="✓ CONFIRM & SAVE", command=finalize_booking, 
                 bg="green", fg="white", font=("Arial", 11, "bold"), width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="✗ CANCEL", command=receipt_window.destroy, 
                 bg="red", fg="white", font=("Arial", 11, "bold"), width=20).pack(side=tk.LEFT, padx=5)

    tk.Button(confirm_frame, text="Confirm Booking", command=confirm_booking, bg="green", fg="white", width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(confirm_frame, text="Cancel", command=seat_window.destroy, width=15).pack(side=tk.LEFT, padx=5)


def show_user_bookings():
    """Display user's booking history and current bookings."""
    if current_user is None:
        messagebox.showerror("Error", "Please login first")
        return

    booking_window = tk.Toplevel()
    booking_window.title(f"My Bookings - {current_user.username}")
    booking_window.geometry("600x450")

    tk.Label(booking_window, text=f"Booking History - {current_user.username}", font=("Arial", 12, "bold")).pack(pady=10)

    if not current_user.bookings:
        tk.Label(booking_window, text="No bookings yet", font=("Arial", 10)).pack(pady=20)
    else:
        text_widget = tk.Text(booking_window, height=18, width=75)
        text_widget.pack(pady=5, padx=5)

        text_widget.insert(tk.END, "=" * 72 + "\n")
        text_widget.insert(tk.END, "YOUR BOOKINGS\n")
        text_widget.insert(tk.END, "=" * 72 + "\n\n")

        for i, booking in enumerate(current_user.bookings, 1):
            text_widget.insert(tk.END, f"Booking #{i}\n")
            text_widget.insert(tk.END, f"  Movie: {booking['movie']}\n")
            text_widget.insert(tk.END, f"  Seats Booked: {booking['seats']}\n")
            text_widget.insert(tk.END, f"  Premiere Date: {booking.get('premiere_date', 'N/A')}\n")
            text_widget.insert(tk.END, f"  Booking Date: {booking.get('booking_date', 'N/A')}\n")
            text_widget.insert(tk.END, "-" * 72 + "\n\n")

        text_widget.config(state=tk.DISABLED)

    tk.Button(booking_window, text="Close", command=booking_window.destroy).pack(pady=10)


#admin panel
def admin_add():
    title = entry_admin_title.get()
    seats = entry_admin_seats.get()
    showtime = entry_admin_showtime.get()
    premiere_date = entry_admin_premiere_date.get()
    if title == "" or seats == "":
        messagebox.showerror("Admin", "Title and seats required")
        return
    try:
        seats_int = int(seats)
    except ValueError:
        messagebox.showerror("Admin", "Seats must be a number")
        return
    success, msg = admin_add_movie(title, seats_int, showtime, premiere_date)
    if success:
        messagebox.showinfo("Admin", msg)
        refresh_movie_list()
    else:
        messagebox.showerror("Admin", msg)


def admin_update():
    title = entry_admin_title.get()
    seats = entry_admin_seats.get()
    showtime = entry_admin_showtime.get()
    premiere_date = entry_admin_premiere_date.get()
    seats_int = None
    if seats != "":
        try:
            seats_int = int(seats)
        except ValueError:
            messagebox.showerror("Admin", "Seats must be a number")
            return
    st = showtime if showtime != "" else None
    pd = premiere_date if premiere_date != "" else None
    success, msg = admin_update_movie(title, seats_int, st, pd)
    if success:
        messagebox.showinfo("Admin", msg)
        refresh_movie_list()
    else:
        messagebox.showerror("Admin", msg)


def admin_remove():
    title = entry_admin_title.get()
    if title == "":
        messagebox.showerror("Admin", "Title required")
        return
    success, msg = admin_remove_movie(title)
    if success:
        messagebox.showinfo("Admin", msg)
        refresh_movie_list()
    else:
        messagebox.showerror("Admin", msg)


def refresh_movie_list():
    movies = admin_list_movies()
    text_movie_list.delete(1.0, tk.END)
    for m in movies:
        text_movie_list.insert(tk.END, f"{m['title']} ({m['seats']} seats) - {m.get('showtime','')} - {m.get('premiere_date','')}\n")

def start_ui():
    global entry_username, entry_password, entry_movie, entry_seats
    global register_button, login_button, label_status, admin_frame
    global register_button, login_button, label_status, admin_frame

    root = tk.Tk()
    root.title("Movie Ticket System")
    root.geometry("300x300")

    label_status = tk.Label(root, text="Not logged in")
    label_status.pack(pady=2)

    label_status = tk.Label(root, text="Not logged in")
    label_status.pack(pady=2)

    tk.Label(root, text="Username").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    register_button = tk.Button(root, text="Register", command=register)
    register_button.pack(pady=5)
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=5)
    register_button = tk.Button(root, text="Register", command=register)
    register_button.pack(pady=5)
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=5)

    tk.Label(root, text="Movie Name").pack()
    entry_movie = tk.Entry(root)
    entry_movie.pack()

    tk.Label(root, text="Seats").pack()
    entry_seats = tk.Entry(root)
    entry_seats.pack()

    tk.Button(root, text="Select Seats & Book", command=show_seat_selection).pack(pady=10)
    tk.Button(root, text="View Movies", command=show_movies).pack(pady=5)
    tk.Button(root, text="My Bookings", command=show_user_bookings).pack(pady=5)

#admin panel (hidden by default, only show for admins after login)
    global admin_frame, entry_admin_title, entry_admin_seats, entry_admin_showtime, entry_admin_premiere_date, text_movie_list
    admin_frame = tk.Frame(root)
    tk.Label(admin_frame, text="Admin Panel", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(admin_frame, text="Title").pack()
    entry_admin_title = tk.Entry(admin_frame)
    entry_admin_title.pack()

    tk.Label(admin_frame, text="Seats").pack()
    entry_admin_seats = tk.Entry(admin_frame)
    entry_admin_seats.pack()

    tk.Label(admin_frame, text="Showtime").pack()
    entry_admin_showtime = tk.Entry(admin_frame)
    entry_admin_showtime.pack()

    tk.Label(admin_frame, text="Premiere Date (YYYY-MM-DD)").pack()
    entry_admin_premiere_date = tk.Entry(admin_frame)
    entry_admin_premiere_date.pack()

    tk.Button(admin_frame, text="Add Movie", command=admin_add).pack(pady=2)
    tk.Button(admin_frame, text="Update Movie", command=admin_update).pack(pady=2)
    tk.Button(admin_frame, text="Remove Movie", command=admin_remove).pack(pady=2)
    tk.Button(admin_frame, text="List Movies", command=refresh_movie_list).pack(pady=2)
    text_movie_list = tk.Text(admin_frame, height=8, width=30)
    text_movie_list.pack(pady=5)
    
    tk.Button(root, text="Select Seats & Book", command=show_seat_selection).pack(pady=10)
    tk.Button(root, text="View Movies", command=show_movies).pack(pady=5)
    tk.Button(root, text="My Bookings", command=show_user_bookings).pack(pady=5)

#admin panel (hidden by default, only show for admins after login)
    global admin_frame, entry_admin_title, entry_admin_seats, entry_admin_showtime, entry_admin_premiere_date, text_movie_list
    admin_frame = tk.Frame(root)
    tk.Label(admin_frame, text="Admin Panel", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(admin_frame, text="Title").pack()
    entry_admin_title = tk.Entry(admin_frame)
    entry_admin_title.pack()

    tk.Label(admin_frame, text="Seats").pack()
    entry_admin_seats = tk.Entry(admin_frame)
    entry_admin_seats.pack()

    tk.Label(admin_frame, text="Showtime").pack()
    entry_admin_showtime = tk.Entry(admin_frame)
    entry_admin_showtime.pack()

    tk.Label(admin_frame, text="Premiere Date (YYYY-MM-DD)").pack()
    entry_admin_premiere_date = tk.Entry(admin_frame)
    entry_admin_premiere_date.pack()

    tk.Button(admin_frame, text="Add Movie", command=admin_add).pack(pady=2)
    tk.Button(admin_frame, text="Update Movie", command=admin_update).pack(pady=2)
    tk.Button(admin_frame, text="Remove Movie", command=admin_remove).pack(pady=2)
    tk.Button(admin_frame, text="List Movies", command=refresh_movie_list).pack(pady=2)
    text_movie_list = tk.Text(admin_frame, height=8, width=30)
    text_movie_list.pack(pady=5)
    
    root.mainloop()
