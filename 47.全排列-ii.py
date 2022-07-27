#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
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
