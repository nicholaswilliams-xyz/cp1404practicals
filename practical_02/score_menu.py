"""
Determine score status and print as many stars as the score
"""


MENU = """S - Input score (0 - 100)
Q - Quit"""


def main():
    print(MENU)
    user_choice = input(">>> ")
    while user_choice != "Q":
        score = float(input("Enter score: "))
        result = return_score_result(score)
        print(result)
        print('*' * round(score))
        print(MENU)
        user_choice = input(">>> ")
    print("Thank you")


def return_score_result(score):
    if 0 <= score < 50:
        return "Bad"

    elif 50 <= score < 90:
        return "Passable"

    elif 90 <= score <= 100:
        return "Excellent"

    else:
        return "Invalid score"


main()
