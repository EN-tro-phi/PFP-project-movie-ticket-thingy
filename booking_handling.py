def create_booking(user, movie_name, seats):

    booking = {
        "movie": movie_name,
        "seats": seats
    }

    user.bookings.append(booking)

    return booking


def get_user_bookings(user):

    return user.bookings
