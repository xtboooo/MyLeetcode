#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
"""
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
