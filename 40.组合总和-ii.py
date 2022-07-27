#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def dfs(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, size):
                if candidates[i] > target:
                    break
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, target - candidates[i])
                path.pop()

        size = len(candidates)
        if not size:
            return []
        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


# @lc code=end
