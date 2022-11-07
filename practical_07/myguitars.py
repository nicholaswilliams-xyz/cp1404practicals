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


if __name__ == "__main__":
    main()
