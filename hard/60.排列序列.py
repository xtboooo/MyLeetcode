#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

1."123"
2."132"
3."213"
4."231"
5."312"
6."321"
给定 n 和 k，返回第 k 个排列。

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
"""


# 内置全排列
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import itertools

        per = list(itertools.permutations(range(1, n + 1)))[k - 1]
        return "".join(map(lambda x: str(x), per))


# dfs+剪枝
class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(path, begin=0):
            nonlocal k
            if begin == n:
                return
            # 所有节点的数量=阶乘
            cnt = factorial[n - 1 - begin]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(path, begin + 1)
                return

        if not n:
            return ""

        used = [False for _ in range(n + 1)]
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            # 预计算阶乘
            factorial[i] = factorial[i - 1] * i
        path = []
        dfs(path)
        return "".join([str(num) for num in path])


# @lc code=end
