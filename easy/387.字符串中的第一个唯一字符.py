#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
"""
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

示例 1：

输入: s = "leetcode"
输出: 0
示例 2:

输入: s = "loveleetcode"
输出: 2
示例 3:

输入: s = "aabb"
输出: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections

        c = collections.Counter(s)
        for i, ch in enumerate(c):
            if c[ch] == 1:
                return i
        return -1


# @lc code=end
