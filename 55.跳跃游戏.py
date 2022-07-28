#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List


# 贪心
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, right_max = len(nums), 0
        for i in range(n):
            if i <= right_max:
                right_max = max(i + nums[i], right_max)
                if right_max >= n - 1:
                    return True
        return False


# @lc code=end
