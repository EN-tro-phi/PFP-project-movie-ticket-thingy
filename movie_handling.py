movies = [
    {"title": "Dune", "seats": 100},
    {"title": "Avatar", "seats": 120},
    {"title": "Interstellar", "seats": 80}
]


def list_movies():
    return movies


def find_movie(title):

    for m in movies:
        if m["title"].lower() == title.lower():
            return m

    return None


def show_movies():
    for m in movies:
        print(m["title"], m["seats"])


def book_ticket(title, n):
    m = find_movie(title)
    if m and m["seats"] >= n:
        m["seats"] -= n
        print("Booked")
    else:
        print("Cannot book")
