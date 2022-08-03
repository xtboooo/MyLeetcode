#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        strs = []
        while columnNumber > 0:
            columnNumber -= 1
            strs.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(strs[::-1])


# @lc code=end
