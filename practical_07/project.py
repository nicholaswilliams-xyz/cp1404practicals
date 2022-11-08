"""

Estimated completion time: 3h
Actual completion time:
"""

from datetime import datetime


class Project:
    """Represent information about projects"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, completion {self.completion_percentage}"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Return TRUE if a project is complete"""
        return self.completion_percentage == 100
