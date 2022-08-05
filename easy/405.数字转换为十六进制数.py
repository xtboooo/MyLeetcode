#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start


CONV = "0123456789abcdef"


# 辗转相除
class Solution1:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        for _ in range(8):
            res.append(num % 16)
            num //= 16
            if not num:
                break
        return "".join([CONV[i] for i in res[::-1]])


# 位运算
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        num &= 0xFFFFFFFF
        while num > 0:
            res.append(CONV[num & 0xF])
            num >>= 4
        return "".join(res[::-1])


# @lc code=end
