"""
Code to test the functionality of class Car() and subclass Taxi()
"""

from taxi import Taxi


def main():
    test_taxi_class()


def test_taxi_class():
    """Demo test code to show how to use Taxi class."""
    my_taxi = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)
    my_taxi.start_fare()
    my_taxi.drive(40)
    print(
        f"Taxi: ${my_taxi.price_per_km}/km, odometer: {my_taxi.current_fare_distance}km, current fare: ${my_taxi.get_fare():0.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(
        f"Taxi: ${my_taxi.price_per_km}/km, odometer: {my_taxi.current_fare_distance}km, current fare: ${my_taxi.get_fare():0.2f}")


if __name__ == "__main__":
    main()
