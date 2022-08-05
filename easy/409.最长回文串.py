#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start

# 贪心


class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections

        c = collections.Counter(s)
        ans = 0
        for v in c.values():
            ans += v // 2 * 2  # 偶数的都取
            if ans % 2 == 0 and v % 2:  # 取奇数+1
                ans += 1
        return ans


# @lc code=end
