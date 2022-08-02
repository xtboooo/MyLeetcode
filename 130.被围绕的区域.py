#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
"""
Medium

给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
示例 2：

输入：board = [["X"]]
输出：[["X"]]
"""
from typing import List


# dfs
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if board[x][y] != "O":
                return
            else:
                board[x][y] = "#"
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    dfs(x + dx, y + dy)

        for i in range(m):
            dfs(i, 0)  # 第一列
            dfs(i, n - 1)  # 最后一列
        for j in range(1, n - 1):
            dfs(0, j)  # 第一行
            dfs(m - 1, j)  # 最后一行
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "#" else "X"


# @lc code=end
