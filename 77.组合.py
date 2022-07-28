#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


# dfs 确定搜索起点
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(begin=1):
            if len(path) == k:
                res.append(path[:])
                return
            upper_bound = n - (k - len(path)) + 1
            for i in range(begin, upper_bound + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        res = []
        path = []
        dfs()
        return res


# dfs 选择or不选择
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(k, begin, path):
            if not k:
                res.append(path)
                return
            # 剪枝
            if begin > n - k + 1:
                return
            # 不选
            dfs(k, begin + 1, path)
            # 选
            dfs(k - 1, begin + 1, path + [begin])

        res = []
        dfs(k, 1, [])
        return res


# @lc code=end
