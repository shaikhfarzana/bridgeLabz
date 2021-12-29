"""
@Author: Farzana Shaikh
@Date: 2021-12-26 19:00:00
@Last Modified by:Farzana Shaikh
@Last Modified time: 2021-12-28 19:00:00
@Title :  Python Program for calculating Sum of three Integer Zero
"""

class py_solution:

    def threeSum(self, nums):
        """
        Description: function to find triplet of zero.
        Parameter:
        self object and int parameter
        Return:
        integer values
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            fwd, rev = i + 1, len(nums) - 1
            while fwd < rev:
                if nums[i] + nums[fwd] + nums[rev] < 0:
                    fwd += 1
                elif nums[i] + nums[fwd] + nums[rev] > 0:
                    rev -= 1
                else:
                    result.append([nums[i], nums[fwd], nums[rev]])
                    fwd, rev = fwd + 1, rev - 1
                    while fwd < rev and nums[fwd] == nums[fwd - 1]:
                        fwd += 1
                    while fwd < rev and nums[rev] == nums[rev + 1]:
                        rev -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


lst = []
n = int(input("Enter the Number of Elements:"))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(py_solution().threeSum(lst))
