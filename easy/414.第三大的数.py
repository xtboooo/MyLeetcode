#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        import heapq

        top_3 = heapq.nlargest(3, set(nums))
        if len(top_3) < 3:
            return top_3[0]
        return top_3[-1]


# @lc code=end
