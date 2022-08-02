#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：


输入：n = 3
输出：5
示例 2：

输入：n = 1
输出：1
"""

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
