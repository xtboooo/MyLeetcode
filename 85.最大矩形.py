#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # 记录当前位置上方连续“1”的个数 多一个0是为了能让元素都出栈
        pre = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0
            # 单调栈
            stack = [-1]
            for k, num in enumerate(pre):
                while stack and num < pre[stack[-1]]:
                    index = stack.pop()
                    res = max(res, pre[index] * (k - stack[-1] - 1))
                stack.append(k)
        return res


# @lc code=end
