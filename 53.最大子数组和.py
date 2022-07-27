#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
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
        pass


# @lc code=end
