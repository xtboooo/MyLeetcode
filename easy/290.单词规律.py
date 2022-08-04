#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
"""
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", s = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", s = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
"""


# 哈希表
class Solution:
    """
    T(n) = O(m+n)
    S(n) = O(m+n)
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        word2ch = {}
        ch2word = {}
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if (ch in ch2word and ch2word[ch] != word) or (
                word in word2ch and word2ch[word] != ch
            ):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True


# @lc code=end
