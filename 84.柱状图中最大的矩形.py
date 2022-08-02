#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
"""
Hard

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：

输入： heights = [2,4]
输出： 4
"""
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
