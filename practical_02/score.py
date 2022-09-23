"""
Determine score status
"""


from random import randint


def main():
    score = float(input("Enter score: "))

    result = return_score_result(score)
    print(result)

    random_score = randint(0, 100)
    random_result = return_score_result(random_score)
    print("\n" + "Random result: " + random_result)


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
