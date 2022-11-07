"""
Read file containing guitar objects. Sort list of guitars
"""

from practical_06.guitar import Guitar

GUITARS = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    """Read file of guitars, save as objects, display."""
    guitars = []
    in_file = open(GUITARS, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[NAME_INDEX], int(parts[YEAR_INDEX]), float(parts[COST_INDEX]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    print("\nAdd a new guitar? (Enter to skip)")
    name = input("Name: ")
    while name != "":
        age = input("Age: ")
        cost = input("cost: ")
        guitar = Guitar(name, int(age), float(cost))
        guitars.append(guitar)
        name = input("Name: ")

    out_file = open(GUITARS, 'w')
    for guitar in guitars:
        print(guitar)
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


if __name__ == "__main__":
    main()
