#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List


# 整体考虑 123 每个元素可选可不选
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, begin):
            if begin == len(nums):
                res.append(path)
                return
            dfs(path, begin + 1)  # 不选
            dfs(path + [nums[begin]], begin + 1)  # 选

        res = []
        dfs([], 0)
        return res


# 顺序考虑 123 先选1 后面可选23
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, begin):
            res.append(path)
            for i in range(begin, len(nums)):
                dfs(path + [nums[i]], i + 1)

        res = []
        dfs([], 0)
        return res


# @lc code=end
