#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(path=[], start=0):
            if start == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    # 剪枝
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(path, start=start + 1)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if not size:
            return []
        nums.sort()
        res = []
        used = [False] * size
        dfs()
        return res


# @lc code=end
