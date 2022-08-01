#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
"""
Easy

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。


示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
"""
from typing import List


# 动态规划
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, max_num = 0, nums[0]
        for x in nums:
            pre = max([pre + x, x])
            max_num = max([pre, max_num])
        return max_num


# 分治
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        ...


# @lc code=end
