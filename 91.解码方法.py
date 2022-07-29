#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
# 基础模型, 爬楼梯, 斐波那契数列
class Solution1:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != "0":
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                f[i] += f[i - 2]
        return f[n]


# 优化, 不新建数组
class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0  # a为两个字母的状态, b为一个字母的状态, c为计算量
            if s[i - 1] != "0":
                c += b
            if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                c += a
            a, b = b, c
        return c


# @lc code=end
