#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
"""
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

示例 1：

输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
示例 2：

输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""


from typing import List


# 异或 掌握
class Solution1:
    def countBits(self, n: int) -> List[int]:
        def count_ones(x: int) -> int:
            ones = 0
            while x > 0:
                x &= x - 1
                ones += 1
            return ones

        return [count_ones(i) for i in range(n + 1)]


# 动态规划 最高有效位
class Solution2:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits


# 动态规划 最低有效位
class Solution3:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits


# 动态规划 最低设置位
class Solution4:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits


# @lc code=end
