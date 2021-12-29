"""
@Author: Farzana Shaikh
@Date: 2021-12-24 13:00:00
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title :  Python3 program to find N-th Harmonic Number

# Function to find N-th Harmonic Number
    # loop to apply the formula
    # Hn = H1 + H2 + H3 ... +
    # Hn-1 + Hn-1 + 1/n
"""


def harmonic_sum(n):
    if n < 1:
        return 0
    else:
        return 1 / n + (harmonic_sum(n - 1))


num = int(input("Enter the number:"))
if num != 0:
    print(harmonic_sum(num))
else:
    print("Number is not valid")
