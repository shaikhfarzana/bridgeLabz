"""
@Author: Farzana Shaikh
@Date: 2021-12-25 18:00:00
@Last Modified by: Farzana Shaikh
@Last Modified time: 2021-12-28 18:00:00
@Title :  Python Program for generating random Coupons
"""

import random


def coupon(x):
    """
    Description:
    function is used to generate distinct coupons.
    Parameter:
    number of digits of coupon
    Return:
    distinct coupon number
     """

    num = '0123456789'
    coupon_no = ''
    for i in range(0, x):
        x = random.randint(0, len(num) - 1)
        coupon_no += num[x: x + 1]
    return coupon_no


num1 = int(input("Enter the Number:"))
print(coupon(num1))

