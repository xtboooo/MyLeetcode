#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag
babgbag
babgbag
babgbag
babgbag
"""


# 动态规划 2d dp
class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        if m > n:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 初始化
        for j in range(n + 1):  # 边界条件
            dp[0][j] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


# 动态规划 1d dp
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        if m > n:
            return 0
        dp = [1] * (n + 1)
        for i in range(1, m + 1):
            # 滚动数组
            dp2 = [0] * (n + 1)
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp2[j] = dp2[j - 1] + dp[j - 1]
                else:
                    dp2[j] = dp2[j - 1]
            dp = dp2
        return dp[-1]


# @lc code=end
