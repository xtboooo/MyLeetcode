#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                step += 1
        return step


# @lc code=end
