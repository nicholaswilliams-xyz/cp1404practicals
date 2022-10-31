"""
Read file. Display champions and their number of victories. Display countries of champions alphabetically
Estimated completion time: 1hr
Actual completion time:
"""

FILENAME = 'wimbledon.csv'
victor_to_wins = {}
winning_countries = set()
wimbledon_data = []


def main():
    in_data = open_file_ignore_header(FILENAME)
    processed_data = process_data(in_data)
    count_victories_per_victor(processed_data)


def open_file_ignore_header(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header row
        in_data = in_file.readlines()
    return in_data


def process_data(in_data):
    for line in in_data:
        line = line.strip('\n').split(',')
        wimbledon_data.append(line)
    return wimbledon_data


def count_victories_per_victor(processed_data):
    for line in processed_data:
        if line[2] in victor_to_wins:  # If champion is already in dictionary, add 1 to their total victories
            victor_to_wins[line[2]] += 1
        else:
            victor_to_wins[line[2]] = 1  # Otherwise, add them to dictionary with 1 victory
        winning_countries.add(line[1])

    print("\nWimbledon Champions:")
    left_align = len(max(victor_to_wins, key=len))
    for name, victories in victor_to_wins.items():
        print(f"{name:<{left_align + 1}}: {victories}")

    print(f"\nThe {len(winning_countries)} countries that won Wimbledon were:")
    print(", ".join(country for country in sorted(winning_countries)))


main()
