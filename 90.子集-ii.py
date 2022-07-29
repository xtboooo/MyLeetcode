#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
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
