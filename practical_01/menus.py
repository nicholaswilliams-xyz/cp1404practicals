"""
Menu displayer
"""
menu = "[H]ello\n" \
       "[G]oodbye\n" \
       "[Q]uit\n"

user_name = input("Enter name: ")

print(menu)

user_choice = input("Enter command: ")

while user_choice != "Q":
       if user_choice == "H":
              print(f"Hello {user_name}")
              print()
       elif user_choice == "G":
              print(f"Goodbye {user_name}")
              print()
       else:
              print("Invalid input")
              print()
       print(menu)
       user_choice = input("Enter command: ")

print("Finished")



