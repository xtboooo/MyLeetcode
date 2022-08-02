#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""


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
