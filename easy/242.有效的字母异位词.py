#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
"""


# 哈希表
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            d[i] = d.get(i, 0) + 1
            d[j] = d.get(j, 0) - 1
        return not any(d.values())


# 计数器
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        if Counter(s) == Counter(t):
            return True
        return False


# @lc code=end
