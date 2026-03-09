from datetime import datetime

def create_booking(user, movie_name, seats, premiere_date=""):

    booking = {
        "movie": movie_name,
        "seats": seats,
        "premiere_date": premiere_date,
        "booking_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    user.bookings.append(booking)

    return booking


def get_user_bookings(user):

    return user.bookings
