"""
Band class
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band."""
        return f"{self.name} ({', '.join([musician.__str__() for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing a band and its musicians and their instruments."""
        for musician in self.musicians:
            return '\n'.join([musician.play() for musician in self.musicians])
