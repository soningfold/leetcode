#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
                if seen[num] > 1:
                    return True
            else:
                seen[num] = 1
        return False
        
# @lc code=end

