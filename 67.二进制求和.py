#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start

# 内置
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"


# 位运算
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]


# @lc code=end
