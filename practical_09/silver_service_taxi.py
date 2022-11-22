"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from practical_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Fancy version of a Taxi that features a flag fall and increased fare costs."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:0.2f}"

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return (self.price_per_km * self.current_fare_distance) + self.flagfall
