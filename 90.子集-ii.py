#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
"""
Medium

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""
from typing import List


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, begin):
            if path not in res:
                res.append(path)
            for i in range(begin, len(nums)):
                if i > begin and nums[i] == nums[i - 1]:
                    continue
                dfs(path + [nums[i]], i + 1)

        nums.sort()
        res = []
        dfs([], 0)
        return res


# 选与不选
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, begin):
            if begin == len(nums):
                res.add(tuple(path))
                return
            dfs(path + [nums[begin]], begin + 1)
            dfs(path, begin + 1)

        nums.sort()
        res = set()
        dfs([], 0)
        return list(res)


# @lc code=end
