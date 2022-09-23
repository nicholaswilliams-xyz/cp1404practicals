"""
A for loop that displays all odd numbers between 1 and 20,
each separated by a space
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()

"---------------- part a. ----------------"
for i in range(0, 100, 10):
    print(i, end=' ')
print()

"---------------- part b. ----------------"
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"---------------- part c. ----------------"
num_stars = int(input("Enter a number: "))

for i in range(num_stars):
    print('*', end='')
print()
print()

"---------------- part d. ----------------"
for i in range(num_stars):
    for j in range(i+1):
        print('*', end='')
    print()