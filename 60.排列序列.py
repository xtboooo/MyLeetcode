#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start

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
