# Here are the objective of this project
# Emplyee/admin should be abe to add, update and delete movies on differnt dates and times
# The employee/users/admin should be able to view the list of movies
# Each movies must have an ID(str), genre(str), name(str), duration(int) and ticket price(float)
# One movie can have mutiple different showtimes on different dates, which the employee/admin can control
# The guest should be able to view the list of movies and their showtimes
# The guest must be able to book tickets for a specific movie at a specific date and time
# New user should have a new user discount of 10% on their first booking after they book their first ticket it would give them the "guest" rank
# the premium user should have a premium discount of 20% on all their bookings (to get premium rank they must pay $100)
# Use JSON to save user data and movie data
# Make a GUI using customtkinter with tkinter


# Note to all
# You should use a extension called "Auto PEP-8", "Pylance", "Python", "Python enviroments", "Python debug" and "Python indent". 
# If its already downloaded onto your extensions then you dont need to download it anymore.

## Admin account & movie management

An **admin user** can manage the movie catalog from the GUI once logged in. The admin panel allows you to:

- **Add a movie** (title, seats and showtime)
- **Update a movie** (change seats and/or showtime)
- **Remove a movie** by title
- **List current movies** with seats and showtimes

To use the admin panel, log in with a user whose `rank` is set to `admin`. The application does not create such a user automatically; you can either:

1. Register a normal user and then edit `users.json` manually, changing the `rank` value to `"admin"`.
2. (Optionally) modify the code to promote a user programmatically.

Movie data is stored in `movies.json` and persists between runs. 
