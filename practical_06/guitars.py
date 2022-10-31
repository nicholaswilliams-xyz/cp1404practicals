"""
Use a list to store all user's guitars
Print guitars' details after user enters a blank name
"""

from practical_06.guitar import Guitar


def main():
    guitars = []
    name = get_name()
    while name != "":
        age = get_year()
        cost = get_cost()
        new_guitar = Guitar(name, age, cost)
        guitars.append(new_guitar)
        name = get_name()
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def get_name():
    """Get name of guitar"""
    name = input("Name: ")
    return name


def get_year():
    """Get year of guitar"""
    done = False
    while not done:
        try:
            age = int(input("Year: "))
            done = True
        except ValueError:
            print("Invalid age. Input integer.")
    return age


def get_cost():
    """Get cost of guitar"""
    done = False
    while not done:
        try:
            cost = int(input("Cost: $"))
            done = True
        except ValueError:
            print("Invalid cost. Enter integer.")
    return cost


main()
