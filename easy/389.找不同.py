#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
"""
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

示例 1：

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
示例 2：

输入：s = "", t = "y"
输出："y"
"""


class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        import collections

        return list(collections.Counter(t) - collections.Counter(s))[0]


# 计数法
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        str_count = [0] * 26
        for ch in s:
            str_count[ord(ch) - ord("a")] += 1
        for ch in t:
            str_count[ord(ch) - ord("a")] -= 1
            if str_count[ord(ch) - ord("a")] < 0:
                return ch


# 求和法
class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


# 异或运算
class Solution4:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s + t:
            res ^= ord(i)
        return chr(res)


# @lc code=end
