#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start

from typing import List


# 两次二分
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect

        m, n = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        row_index = bisect.bisect_right(col0, target) - 1  # 从右边寻找目标元素在列表中的有序位置
        if row_index < 0:
            return False
        col_index = bisect.bisect_left(matrix[row_index], target)
        if col_index >= n:  # >超过最大值, =介于最大和次大值之间
            return False
        if matrix[row_index][col_index] == target:
            return True
        return False


# 一次二分
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            curr = matrix[mid // n][mid % n]
            if curr == target:
                return True
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


# @lc code=end
