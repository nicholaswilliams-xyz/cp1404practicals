"""
Store users' emails and names in a dictionary. Ask user for emails until no characters are entered.
Estimated completion time: 40m
Actual completion time: 34m
"""

NAME_TO_EMAIL = {}

email = input("Email: ")
while email != "":
    name_before_at = ' '.join((email.split('@')[0]).title().split('.'))

    is_name_correct = input(f"Is your name {name_before_at}? (Y/N): ")

    if is_name_correct.lower() == 'y' or is_name_correct.lower() == '':
        NAME_TO_EMAIL[name_before_at] = email
    else:
        proper_name = input("Name: ")
        NAME_TO_EMAIL[proper_name] = email

    email = input("Email: ")

left_align = len(max(NAME_TO_EMAIL, key=len))

for name, email in NAME_TO_EMAIL.items():
    print(f"{name:<{left_align + 1}}: {email}")
