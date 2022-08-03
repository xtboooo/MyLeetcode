#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start

# 进制
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for i, ch in enumerate(columnTitle[::-1]):
            offset = ord(ch) - ord("A") + 1
            num += 26**i * offset if num else offset
        return num


# @lc code=end
