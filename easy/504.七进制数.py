#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
"""
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:

输入: num = 100
输出: "202"
示例 2:

输入: num = -7
输出: "-10"
"""

# 辗转相除法
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append("-")
        return "".join(reversed(digits))


# @lc code=end
