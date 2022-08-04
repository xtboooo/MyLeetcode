#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"
"""


# 双指针
class Solution:
    """
    T(n) = O(n)
    S(n) = O(1)
    """

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        chs = "aeiouAEIOU"
        while left <= right:
            if s[left] in chs and s[right] in chs:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in chs:
                right -= 1
            elif s[right] in chs:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)


# @lc code=end
