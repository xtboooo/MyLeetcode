#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
"""
对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。

例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
给你一个整数 num ，输出它的补数。

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
"""


# 累加0位
class Solution1:
    def findComplement(self, num: int) -> int:
        i = ans = 0
        while num:
            if not num & 1:
                ans += 1 << i
            num >>= 1
            i += 1
        return ans


# 整数+补数 = 满位数-1
class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** (len(bin(num)) - 2) - num - 1


# @lc code=end
