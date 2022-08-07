#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]
示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        board = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []
        for word in words:
            tmp = set(word.lower())
            # if any(tmp.issubset(row) for row in board):
            #     res.append(word)
            for row in board:
                if word.lower()[0] in row and tmp.issubset(row):
                    res.append(word)
        return res


# @lc code=end
