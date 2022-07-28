#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


# 模拟
class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


# 分层
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


# 神仙
class Solution3:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


# @lc code=end
