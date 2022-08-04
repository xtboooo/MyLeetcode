#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections

        if len(ransomNote) > len(magazine):
            return False
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        return not r - m


# @lc code=end
