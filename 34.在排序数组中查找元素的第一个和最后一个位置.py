#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
"""
Medium

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        if not nums:
            return [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                M, R = mid, right
                # left right 为相同target的上下界
                # 左边
                right = M
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        right = mid - 1
                    else:
                        left = mid + 1
                left_ans = left
                # 右边
                left, right = M, R
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        left = mid + 1
                    else:
                        right = mid - 1
                right_ans = right
                return [left_ans, right_ans]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]


# @lc code=end
