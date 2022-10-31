"""

Start date: 31.10.2022
Start time: 18:25
Estimated completion time: 30 minutes
Actual completion time: 18:44
"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, typing="", reflection="", year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return 1
        else:
            return 0

