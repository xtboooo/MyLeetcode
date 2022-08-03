#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""
from typing import List


# 异或运算
class Solution:
    """
    T(n) = O(n)
    S(n) = O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        import functools

        return functools.reduce(lambda x, y: x ^ y, nums)


# @lc code=end
