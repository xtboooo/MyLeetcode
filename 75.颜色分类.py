#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
"""
Medium

给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
"""
from typing import List


# 单指针
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        return nums


# 单向双指针
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr0 = ptr1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[ptr1], nums[i] = nums[i], nums[ptr1]
                ptr1 += 1
            elif nums[i] == 0:
                nums[ptr0], nums[i] = nums[i], nums[ptr0]
                if ptr0 < ptr1:
                    nums[ptr1], nums[i] = nums[i], nums[ptr1]
                ptr1 += 1
                ptr0 += 1
        return nums


# 双向双指针
class Solution3:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr0, ptr2 = 0, n - 1
        i = 0
        while i <= ptr2:
            while i <= ptr2 and nums[i] == 2:  # 这个while保证从左向右扫描的2可以被正确交换
                nums[ptr2], nums[i] = nums[i], nums[ptr2]
                ptr2 -= 1
            if nums[i] == 0:
                nums[ptr0], nums[i] = nums[i], nums[ptr0]
                ptr0 += 1
            i += 1
        return nums


# @lc code=end
