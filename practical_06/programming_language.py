"""
Programming language Class

Start time: 18:25
Estimated completion time: 30 minutes
Actual completion time: 50 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return f string of the attributes of a programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """If the programming language is dynamically-typed, return 1. Otherwise, return 0."""
        if self.typing == "Dynamic":
            return 1
        else:
            return 0
