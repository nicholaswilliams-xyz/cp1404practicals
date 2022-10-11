"""
Prompt user for 5 numbers and append numbers to list. Print information based on numbers
"""


numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    get_numbers()
    print_interesting_things()
    check_username()


def get_numbers():
    for i in range(5):
        user_number = int(input("Input any number: "))
        numbers.append(user_number)


def print_interesting_things():
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {(sum(numbers)/len(numbers))}")


def check_username():
    user_name = input("Input username: ")
    if user_name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
