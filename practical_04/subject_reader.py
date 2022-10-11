"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
list_of_lines = []


def main():
    data = get_data()
    print(f"data")
    print_formatted_list()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")

        list_of_lines.append(parts)  # Append each list to the list of lines
        print(list_of_lines)
    input_file.close()
    return list_of_lines


def print_formatted_list():
    for data in list_of_lines:
        print(f"{data[0]} is taught by {data[1]} and has {data[2]} students")


main()
