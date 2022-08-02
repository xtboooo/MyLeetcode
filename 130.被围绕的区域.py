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
class Solution1:
    """
    T(n) = O(m*n)
    S(n) = O(m*n)
    """

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


# bfs
class Solution2:
    """
    T(n) = O(m*n)
    S(n) = O(m*n)
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def bfs(x, y):
            import collections

            q = collections.deque()
            q.append((x, y))
            while q:
                x, y = q.pop()
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    board[x][y] = "#"
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        q.appendleft((x + dx, y + dy))

        for i in range(m):
            bfs(i, 0)  # 第一列
            bfs(i, n - 1)  # 最后一列
        for j in range(1, n - 1):
            bfs(0, j)  # 第一行
            bfs(m - 1, j)  # 最后一行
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "#" else "X"


# 查并集 (测试不太行 280ms) https://blog.csdn.net/weixin_43455338/article/details/106143255
class Solution3:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        m = len(board)
        n = len(board[0])
        if not m or not n:
            return
        dummy = m * n
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        union(i * n + j, dummy)
                    else:
                        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            if board[i + x][j + y] == "O":
                                union(i * n + j, (i + x) * n + (j + y))
        for i in range(m):
            for j in range(n):
                if find(dummy) == find(i * n + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


# @lc code=end
