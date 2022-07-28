#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List


# 维护访问数组
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    if not (new_i, new_j) in visited:
                        if check(new_i, new_j, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False


# 直接修改原数组
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])

        def dfs(i, j, index):
            if board[i][j] != word[index]:
                return False  # 剪枝
            if index == len(word) - 1:
                return True
            board[i][j] = "*"
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and dfs(new_i, new_j, index + 1)
                ):
                    return True
            board[i][j] = word[index]  # 还原

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end
