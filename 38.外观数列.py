#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start


class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for _ in range(n - 1):
            curr = ""
            pos = 0
            start = 0
            while pos < len(prev):
                while pos < len(prev) and prev[start] == prev[pos]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr
        return prev


# @lc code=end
