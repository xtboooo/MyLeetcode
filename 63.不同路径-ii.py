#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List


# dfs
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            if obstacleGrid[i][j] or i < 0 or j < 0:
                return 0
            return dfs(i - 1, j) + dfs(i, j - 1) if i or j else 1

        return dfs(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)


# 动态规划
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """_summary_

        Args:
            obstacleGrid (List[List[int]]): _description_

        Returns:
            int: _description_
        """
        # 定义状态：即数据元素的含义：dp表示当前位置的路径条数
        # 建立状态转移方程：dp[i] = dp[i]+dp[i-1]
        # 设定初始值：增加初始值1，即dp = [1] + [0]*n
        # 状态压缩：即优化数组空间,将二维数组压缩到一维数组,逐行计算当前最新路径条数，并覆盖上一行对应的路径条数
        # 选取dp[-2]表示到达finish位置路径总条数,因为一开始新增加的1,因此最终值要往前推一个

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[-2]


# @lc code=end
