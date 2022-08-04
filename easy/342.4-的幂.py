#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

示例 1：

输入：n = 16
输出：true
示例 2：

输入：n = 5
输出：false
示例 3：

输入：n = 1
输出：true
"""


# 二进制表示中 1 的位置
class Solution1:
    """
    T(n) = O(1)
    S(n) = O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        # 0xAAAAAAAA : (10101010101010101010101010101010)2
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0


# 取模性质
class Solution2:
    """
    T(n) = O(1)
    S(n) = O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1


# @lc code=end
