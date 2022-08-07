#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
"""
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

给定一个 整数 n， 如果是完美数，返回 true；否则返回 false。

示例 1：

输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
示例 2：

输入：num = 7
输出：false
"""

# 枚举
class Solution1:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 1
        for i in range(2, int(num**0.5) + 1):
            x, y = divmod(num, i)
            if y == 0:
                res += i + x
        return res == num


# 数学
class Solution2:
    def checkPerfectNumber(self, num: int) -> bool:
        return (
            num == 6
            or num == 28
            or num == 496
            or num == 8128
            or num == 33550336
        )


# @lc code=end
