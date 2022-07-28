#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start

# 暴力递归
class Solution1:
    import functools

    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# dfs
class Solution2:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i == 0 or i == 1:
                return 1
            if record[i] == -1:
                record[i] = dfs(i - 1) + dfs(i - 2)
            return record[i]

        record = [-1] * (n + 1)
        return dfs(n)


# 动态规划, 就地改变, 斐波那契实现
class Solution3:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# @lc code=end
