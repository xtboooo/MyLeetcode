#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = []
        for li, ri in intervals:
            if li > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                ans.append([li, ri])
            else:
                left = min(li, left)
                right = max(ri, right)
        if not placed:
            ans.append([left, right])
        return ans


# @lc code=end
