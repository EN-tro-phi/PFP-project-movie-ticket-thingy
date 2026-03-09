from json_storage import load_movies, save_movies

movies = load_movies()
if not movies:
    movies = [
        {"title": "Dune", "seats": 100, "showtime": "8pm", "premiere_date": "2024-02-15"},
        {"title": "Avatar", "seats": 120, "showtime": "9pm", "premiere_date": "2024-03-01"},
        {"title": "Interstellar", "seats": 80, "showtime": "7pm", "premiere_date": "2024-02-28"}
    ]
    save_movies(movies)


def list_movies():
    return movies


def find_movie(title):
    for m in movies:
        if m["title"].lower() == title.lower():
            return m

    return None


def add_movie(title, seats, showtime="", premiere_date=""):
    if find_movie(title):
        return False, "Movie already exists"
    new_m = {"title": title, "seats": seats, "showtime": showtime, "premiere_date": premiere_date}
    movies.append(new_m)
    save_movies(movies)
    return True, "Movie added"


def remove_movie(title):
    m = find_movie(title)
    if not m:
        return False, "Movie not found"
    movies.remove(m)
    save_movies(movies)
    return True, "Movie removed"


def update_movie(title, seats=None, showtime=None, premiere_date=None):
    m = find_movie(title)
    if not m:
        return False, "Movie not found"
    if seats is not None:
        m["seats"] = seats
    if showtime is not None:
        m["showtime"] = showtime
    if premiere_date is not None:
        m["premiere_date"] = premiere_date
    save_movies(movies)
    return True, "Movie updated"


def book_ticket(title, n):
    m = find_movie(title)
    if not m:
        return False, "Movie not found"
    if m["seats"] < n:
        return False, "Not enough seats"
    m["seats"] -= n
    save_movies(movies)
    return True, "Booked"
