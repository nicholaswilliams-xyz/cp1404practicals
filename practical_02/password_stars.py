"""
Ask user for password. Print as many asterisks as there are characters in the password
"""


def main():
    user_password = get_password()
    print_asterisks(user_password)


def get_password():
    user_password = input("Input password: ")
    min_password_length = 5
    while len(user_password) <= min_password_length:
        print(f"Error: password to short. Enter password of more than {min_password_length} characters")
        user_password = input("Input password: ")
    return user_password


def print_asterisks(user_password):
    print('*' * len(user_password))


main()
