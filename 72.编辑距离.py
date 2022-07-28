#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start

# 动态规划, 一维数组
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = list(range(n + 1))
        for i in range(m):
            left_up = dp[0]
            dp[0] = i + 1
            for j in range(n):
                dp[j + 1], left_up = (
                    min(
                        dp[j] + 1,
                        dp[j + 1] + 1,
                        left_up + (int(word1[i] != word2[j])),
                    ),
                    dp[j + 1],
                )
        return dp[-1]


# 动态规划, 二维数组
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # 有一个字符串为空串
        if m * n == 0:
            return m + n
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)

        return dp[n][m]


# @lc code=end
