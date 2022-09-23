"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

under_1000_bonus = float(0.1)
over_1000_bonus = float(0.15)

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales >= 1000:
        bonus = over_1000_bonus * sales
        print("Your bonus is ${:.2f}".format(bonus))
    else:
        bonus = under_1000_bonus * sales
        print("Your bonus is ${:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))


