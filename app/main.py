from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []

    for cus in customers:
        customer = Customer(name=cus["name"], food=cus["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(
            product=cus["food"],
            customer=customer
        )

    new_cleaner = Cleaner(cleaner)

    new_cinema_hall = CinemaHall(number=hall_number)
    new_cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=new_cleaner
    )
