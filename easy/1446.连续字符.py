#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        ans, count = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
        return ans


# @lc code=end
