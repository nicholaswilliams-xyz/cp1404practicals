"""
Ask user for number of "quick picks". Generate this number of lines consisting
of 6 random number between 1 and 45
"""


from random import randint


NUMBERS_PER_LINE = 6
MIN_RANDOM = 1
MAX_RANDOM = 45


def main():
    print_quick_picks()


def print_quick_picks():
    number_of_quick_picks = int(input("How many quick picks?: "))
    for row in range(number_of_quick_picks):
        quick_picks = []
        number_of_numbers = 0
        while number_of_numbers != 6:
            random_number = randint(MIN_RANDOM, MAX_RANDOM)
            if not (random_number in quick_picks):
                quick_picks.append(random_number)
                number_of_numbers += 1
        print("".join("{:>3}".format(number) for number in sorted(quick_picks)))


main()
