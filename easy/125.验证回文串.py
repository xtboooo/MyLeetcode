#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串
"""


# 倒序检验
class Solution1:
    """
    T(n) = O(|s|)
    S(n) = O(|s|)
    """

    def isPalindrome(self, s: str) -> bool:
        is_good = "".join(ch.lower() for ch in s if ch.isalnum())
        return is_good == is_good[::-1]


# 双指针检验
class Solution2:
    """
    T(n) = O([s])
    S(n) = O(|s|)
    """

    def isPalindrome(self, s: str) -> bool:
        is_good = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(is_good)
        left, right = 0, n - 1
        while left < right:
            if is_good[left] != is_good[right]:
                return False
            left += 1
            right -= 1
        return True


# 双指针检验
class Solution3:
    """
    T(n) = O(|s|)
    S(n) = O(1)
    """

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True


# @lc code=end
