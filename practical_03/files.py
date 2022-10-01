"""
Open file and read contents
"""


def main():
    create_name_file()
    read_name_file()
    read_and_add_two_numbers()
    read_and_add_all_numbers()


def create_name_file():
    user_name = input("Enter name: ")
    out_file = open("name.txt", 'w')
    print(f"{user_name}", file=out_file)
    out_file.close()


def read_name_file():
    in_file = open("name.txt", 'r')
    line = in_file.read()
    in_file.close()
    print(f"Your name is {line}")


def read_and_add_two_numbers():
    in_file = open("numbers.txt", 'r')
    sum_first_two_nums = 0
    for i in range(2):
        line = int(in_file.readline())
        sum_first_two_nums = sum_first_two_nums + line
    in_file.close()
    print(f"{sum_first_two_nums}")


def read_and_add_all_numbers():
    in_file = open("numbers.txt", 'r')
    sum_all_nums = 0
    for line in in_file:
        sum_all_nums = sum_all_nums + int(line)
    in_file.close()
    print(f"{sum_all_nums}")


main()
