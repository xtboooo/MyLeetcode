#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start

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
