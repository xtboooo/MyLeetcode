#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def dfs(start, path, target):
            if target == 0:
                res.append(path)
                return
            for i in range(start, size):
                last = target - candidates[i]
                if last < 0:
                    break
                dfs(i, path + [candidates[i]], last)

        candidates.sort()

        size = len(candidates)
        if not size:
            return []
        path = []
        res = []
        dfs(0, path, target)
        return res


# @lc code=end
