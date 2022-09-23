"""
Determine score status and print as many stars as the score
"""


from random import randint


def main():
    score = float(input("Enter score: "))

    result = return_score_result(score)
    print(result)
    print('*' * round(score))


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
