#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
"""
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6
"""
from typing import List


# 排序
class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]
        )


# 打擂台
class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = float("-inf")
        d = e = float("inf")
        for i, num in enumerate(nums):
            # 更新最大三个数
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
            # 更新最小两个数
            if num < d:
                d, e = num, d
            elif num < e:
                e = num
        return max(d * e * a, a * b * c)


# @lc code=end
