"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from practical_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability of a car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()}, {self.reliability}"

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
