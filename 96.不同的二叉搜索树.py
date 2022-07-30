#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start

from functools import cache


# 递归
class Solution1:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            ans = 0
            for i in range(n):
                ans += self.numTrees(i) * self.numTrees(n - i - 1)
            return ans


# 动态规划
class Solution2:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[-1]


# @lc code=end
