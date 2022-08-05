#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
from typing import List


# 数学 https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-tt3zu/
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


# @lc code=end
