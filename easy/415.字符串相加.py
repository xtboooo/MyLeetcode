#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1 = list(map(int, num1))[::-1]
        s2 = list(map(int, num2))[::-1]
        i = summ = addd = 0
        res = ""
        while max(len(num1), len(num2)) > i:
            a = 0 if i >= len(s1) else s1[i]
            b = 0 if i >= len(s2) else s2[i]
            summ = (addd + a + b) % 10
            addd = (addd + a + b) // 10
            res = str(summ) + res
            i += 1
        if addd:
            res = "1" + res
        return res


# @lc code=end
