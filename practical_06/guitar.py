"""
Use a class to store guitars

Estimated completion time:
Actual completion time:
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0.00):
        """Initialise values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return f-string of guitar object attributes"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Return a guitar's age in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return true if a guitar is a vintage. Otherwise, return false"""
        return self.get_age() >= VINTAGE_AGE


def main():
