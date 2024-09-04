#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        p1, p2 = 0, 1
        expected_dif = 1
        ranges_arr = []
        while p2 < len(nums) + 1:
            if nums[min(p2, len(nums) - 1)] - nums[p1] == expected_dif:
                p2 += 1
                expected_dif += 1
            else:
                if expected_dif == 1:
                    ranges_arr.append(f'{nums[p1]}')
                else:
                    ranges_arr.append(f'{nums[p1]}->{nums[p2 - 1]}')
                p1 = p2
                p2 += 1
                expected_dif = 1
        return ranges_arr



# @lc code=end
