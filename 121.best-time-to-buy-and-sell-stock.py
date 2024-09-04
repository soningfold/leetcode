#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        smallest = float('inf')
        for num in prices:
            if num < smallest:
                smallest = num
            if max_profit < num - smallest:
                max_profit = num - smallest
        return max_profit

# @lc code=end

