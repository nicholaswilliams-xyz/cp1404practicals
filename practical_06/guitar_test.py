"""
Test Guitar class

Estimated completion time:
Actual completion time:
"""

from guitar import Guitar

my_martinez = Guitar("Martinez MDC-20A-NGL", 2018, 400)

print(f"{my_martinez.name} get_age(). Expected 4. Got {my_martinez.get_age()}")
print(f"{my_martinez.name} is_vintage(). Expected False. Got {my_martinez.is_vintage()}")

if my_martinez.is_vintage():
    print("Boy, you have an old guitar alright")
else:
    print("The sound of your guitar will grow richer with time")
