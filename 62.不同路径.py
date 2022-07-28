#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# 动态规划
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


# 组合数学
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        import math

        return math.comb(m + n - 2, n - 1)


# @lc code=end
