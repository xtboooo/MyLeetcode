#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
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
