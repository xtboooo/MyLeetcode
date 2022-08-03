#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]


# @lc code=end
