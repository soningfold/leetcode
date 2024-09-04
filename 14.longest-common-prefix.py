#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ''
        if len(strs) == 1:
            return strs[0]
        try:
            current_prefix = strs[0][0]
            count = 0
            i = 0
            while True:
                if not strs[i][count] == current_prefix:
                    break
                if i == len(strs) - 1:
                    common_prefix += current_prefix
                    count += 1
                    current_prefix = strs[0][count]
                    i = 0
                i += 1
            return common_prefix
            
        finally:
            return common_prefix
        
# @lc code=end

