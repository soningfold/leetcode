#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        jewels_dict = {jewel : 0 for jewel in jewels}
        for stone in stones:
            if stone in jewels_dict:
                total += 1
        return total
        
# @lc code=end

