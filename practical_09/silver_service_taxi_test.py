"""
Code to test the functionality of class Car() and subclass Taxi()
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    test_taxi_class()


def test_taxi_class():
    """Demo test code to show how to use SilverServiceTaxi class."""

    "Test __str__ method"
    my_hummer = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)
    print(my_hummer)

    "Test for the proper calculation of fares for an 18km trip"
    my_silver_taxi = SilverServiceTaxi(name="Prius 1", fuel=100, fanciness=2)
    my_silver_taxi.start_fare()
    my_silver_taxi.drive(18)
    print(
        f"Taxi: ${my_silver_taxi.price_per_km}/km, odometer: {my_silver_taxi.current_fare_distance}km, current fare: ${my_silver_taxi.get_fare():0.2f}")


if __name__ == "__main__":
    main()
