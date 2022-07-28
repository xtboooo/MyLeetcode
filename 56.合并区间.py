#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                # 不可合并
                merged.append(interval)
            else:
                # 可合并
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged


# @lc code=end
