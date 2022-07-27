#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

from collections import defaultdict
from math import sqrt
from typing import List


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0: row, 1: column, 2: square
        record = {
            0: defaultdict(set),
            1: defaultdict(set),
            2: defaultdict(set),
        }
        n = len(board)
        m = sqrt(n)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in record[0][i] or board[i][j] in record[1][j]:
                    return False
                sq = i // m * m + j // m
                if board[i][j] in record[2][sq]:
                    return False
                record[0][i].add(board[i][j])
                record[1][j].add(board[i][j])
                record[2][sq].add(board[i][j])
        return True


# @lc code=end
