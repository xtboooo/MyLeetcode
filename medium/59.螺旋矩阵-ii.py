#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):  # 左到右
                matrix[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):  # 上到下
                matrix[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):  # 右到左
                matrix[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):  # 下到上
                matrix[i][l] = num
                num += 1
            l += 1
        return matrix


# @lc code=end
