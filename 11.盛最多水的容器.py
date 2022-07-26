#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from selectors import EpollSelector
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, i, j = 0, 0, len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                res = height[i] * (j - i)
                i += 1
            else:
                res = height[j] * (j - i)
                j -= 1
            if res > ans:
                ans = res
        return ans


# @lc code=end
