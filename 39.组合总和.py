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
                res.append(path[:])
                return
            for i in range(start, size):
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i, path, target - candidates[i])
                path.pop()

        candidates.sort()

        size = len(candidates)
        if not size:
            return []
        path = []
        res = []
        dfs(0, path, target)
        return res


# @lc code=end
