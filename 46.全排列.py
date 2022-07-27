#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#


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
