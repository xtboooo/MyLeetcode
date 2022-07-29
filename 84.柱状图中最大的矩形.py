#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List


# 单调栈 未优化
class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        res = 0
        for i in range(n):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                while len(stack) > 0 and curr_height == heights[stack[-1]]:
                    stack.pop()
                if len(stack) > 0:
                    curr_width = i - stack[-1] - 1
                else:
                    curr_width = i
                res = max(res, curr_height * curr_width)
            stack.append(i)
        while len(stack) > 0:
            curr_height = heights[stack.pop()]
            while len(stack) > 0 and curr_height == heights[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                # stack中索引严格递增, 对应的高度严格递增
                curr_width = n - stack[-1] - 1
            else:
                curr_width = n
            res = max(res, curr_height * curr_width)
        return res


# 优化  添加哨兵节点
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = [0]
        res = 0
        n = len(heights)

        for i in range(1, n):
            while heights[i] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                res = max(res, curr_height * curr_width)
            stack.append(i)
        return res


# @lc code=end
