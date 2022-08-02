#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""
from typing import List


# 动态规划, 整体纵向填充
class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)
        for i in range(n):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max = [0] * (n - 1) + [height[-1]]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        return sum(
            min(left_max[i], right_max[i]) - height[i] for i in range(n)
        )


# # 单调栈, 横向填充
class Solution2:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                # 前一个方块的高度索引
                top = stack.pop()
                if not stack:
                    break
                # 最左侧方格的高度索引
                left = stack[-1]
                curr_width = i - left - 1
                curr_height = min(h, height[left]) - height[top]
                ans += curr_width * curr_height
            stack.append(i)
        return ans


# 双指针 单列纵向填充
class Solution3:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans


# @lc code=end
