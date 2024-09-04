#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        sorted_strings = []
        n = len(strs)
        for string in strs:
            sorted_strings.append("".join(sorted(string)))

        seen = {}
        for i in range(n):
            if sorted_strings[i] in seen:
                pass
            else:
                seen[sorted_strings[i]] = 1

        for key in seen:
            anag_group = []
            for i in range(n):
                if sorted_strings[i] == key:
                    anag_group.append(strs[i])
            result.append(anag_group)
        return result
        
# @lc code=end

