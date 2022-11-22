"""
Taxi simulator to allow customer to drive a taxi of their choosing
"""

from practical_09.silver_service_taxi import SilverServiceTaxi
from practical_09.taxi import Taxi

MENU = """
q)uit, c)hoose, d)rive
>>> """

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Present user with a list of available taxis.
    Allow them to drive that taxi a desired distance.
    Display cumulative bill. Repeat until user quits."""
    total_bill = 0
    user_choice = input(MENU)
    while user_choice.lower() != "q":
        if user_choice.lower() == "c":
            taxi_choice = choose_taxi()
        elif user_choice.lower() == "d":
            try:
                total_bill = drive_taxi(taxi_choice, total_bill)
            except UnboundLocalError:
                print("Choose a taxi before driving")
        else:
            print("Invalid choice")
        print(f"Bill to date: {total_bill:0.2f}")
        user_choice = input(MENU)


def choose_taxi():
    """Display available taxis and obtain taxi choice from user"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = get_valid_index("Choose taxi: ", len(taxis))
    return taxi_choice


def drive_taxi(taxi_choice, total_bill):
    """Obtain distance from user to be driven in chosen taxi. Calculate and return cumulative bill"""
    driving_distance = get_valid_distance("Drive how far?: ")
    taxis[taxi_choice].drive(driving_distance)
    print(f"Your {taxis[taxi_choice].name} trip will cost you ${taxis[taxi_choice].get_fare() - total_bill:0.2f}")
    total_bill += taxis[taxi_choice].get_fare()
    return total_bill


def get_valid_index(prompt, array_length):
    """Make sure user-inputted index choice fits is valid regarding the specified array"""
    done = False
    while not done:
        try:
            index = int(input(prompt))
            if 0 <= index <= (array_length - 1):
                done = True
            else:
                print("Invalid choice")
        except ValueError:
            done = False
            print("Invalid choice")
    return index


def get_valid_distance(prompt):
    """Make sure user-inputted distance is a positive number"""
    done = False
    while not done:
        try:
            distance = float(input(prompt))
            if distance > 0:
                done = True
            else:
                print("Invalid distance")
        except ValueError:
            done = False
            print("Invalid distance")
    return distance


if __name__ == "__main__":
    main()
