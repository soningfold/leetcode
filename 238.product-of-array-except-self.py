#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        prefix_arr = []
        for num in nums:
            prefix = num * product
            prefix_arr.append(prefix)
            product = prefix
        print(prefix_arr)
# @lc code=end

