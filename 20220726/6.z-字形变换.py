#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):  # 枚举矩阵的行
            for j in range(0, n - i, t):  # 枚举每个周期的起始下标
                ans.append(s[j + i])  # 当前周期的第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])  # 当前周期的第二个字符
        return "".join(ans)


# @lc code=end
