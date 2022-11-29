"""
Code to test the functionality of class Car() and subclass Taxi()
"""

from unreliable_car import UnreliableCar


def main():
    test_unreliable_car_class()


def test_unreliable_car_class():
    """Demo test code to show how to use Taxi class."""
    shot_car = UnreliableCar(name="Shot Car", fuel=100, reliability=10)
    shot_car.drive(40)
    print(f"{shot_car}")


if __name__ == "__main__":
    main()
