#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1
"""
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
