#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_hash, magazine_hash = {}, {}

        for letter in ransomNote:
            if letter not in ransom_hash:
                ransom_hash[letter] = 1
            else:
                ransom_hash[letter] += 1
        
        for letter in magazine:
            if letter not in magazine_hash:
                magazine_hash[letter] = 1
            else:
                magazine_hash[letter] += 1

        for key in ransom_hash:
            if key in magazine_hash and ransom_hash[key] <= magazine_hash[key]:
                pass
            else:
                return False
        return True
        
# @lc code=end

