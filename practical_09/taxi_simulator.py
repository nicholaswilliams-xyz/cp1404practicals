"""
Taxi simulator to allow customer to drive a taxi of their choosing
"""

from practical_09.silver_service_taxi import SilverServiceTaxi
from practical_09.taxi import Taxi

MENU = """q)uit, c)hoose, d)rive
>>> """

total_bill = 0
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    user_choice = input(MENU)
    while user_choice.lower() != "q":
        if user_choice.lower() == "c":
            taxi_choice = choose_taxi()
        elif user_choice.lower() == "d":
            try:
                print("Function to be added")
            except UnboundLocalError:
                print("Choose a taxi before driving")
        else:
            print("Invalid choice")
        print(f"Bill to date: {total_bill}")
        user_choice = input(MENU)


def choose_taxi():
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = get_valid_index("Choose taxi: ", len(taxis))
    return taxi_choice


def get_valid_index(prompt, array_length):
    done = False
    while not done:
        try:
            index = int(input(prompt))
            if 0 <= index <= (array_length - 1):
                done = True
        except ValueError:
            done = False
        print("Invalid choice")
    return index


if __name__ == "__main__":
    main()
