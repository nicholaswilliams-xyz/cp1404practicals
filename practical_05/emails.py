"""
Store users' emails and names in a dictionary. Ask user for emails until no characters are entered.
Estimated completion time: 40m
Actual completion time: 34m
"""

name_to_email = {}

email = input("Email: ")
while email != "":
    name_before_at = ' '.join((email.split('@')[0]).title().split('.'))

    is_name_correct = input(f"Is your name {name_before_at}? (Y/N): ")

    if is_name_correct.lower() == 'y' or is_name_correct == '':
        name_to_email[name_before_at] = email
    else:
        proper_name = input("Name: ")
        name_to_email[proper_name] = email

    email = input("Email: ")

left_align = len(max(name_to_email, key=len))

for name, email in name_to_email.items():
    print(f"{name:<{left_align + 1}}: {email}")
