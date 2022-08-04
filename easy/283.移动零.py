#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""


from typing import List


class Solution:
    """
    T(n) = O(n)
    S(n) = O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            # 保证left-right区间都是0
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1


# @lc code=end
