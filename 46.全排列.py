#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

"""
Medium

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""
from itertools import permutations
from typing import List


# @lc code=start
# # 内置库 C实现
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


# 回溯
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrace(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrace()
        return res


# @lc code=end
