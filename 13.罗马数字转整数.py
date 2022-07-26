#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    SYMBOL_VALUES = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, str in enumerate(s):
            value = Solution.SYMBOL_VALUES[str]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans


# @lc code=end
