#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start


"""
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

示例 1：

输入：num = 16
输出：true
示例 2：

输入：num = 14
输出：false
"""


# pow
class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        return float.is_integer(num**0.5)


# 二分法
class Solution2:
    """
    T(O) = O(log n)
    S(O) = O(1)
    """

    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            if mid**2 < num:
                l = mid + 1
            elif mid**2 > num:
                r = mid - 1
            else:
                return True
        return False


# @lc code=end
