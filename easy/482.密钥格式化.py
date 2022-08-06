#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        ans = ""
        for i in range(0, len(s), k):
            ans += s[i : i + k] + "-"
        return ans[::-1].lstrip("-")


# @lc code=end
