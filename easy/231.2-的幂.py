#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

示例 1：

输入：n = 1
输出：true
解释：20 = 1
示例 2：

输入：n = 16
输出：true
解释：24 = 16
示例 3：

输入：n = 3
输出：false
示例 4：

输入：n = 4
输出：true
示例 5：

输入：n = 5
输出：false
"""


# 移除最低次位的1
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bool(n & (n - 1))


# 另一种写法
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n


# 直接算约数
class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 2**30 % n == 0


# @lc code=end
