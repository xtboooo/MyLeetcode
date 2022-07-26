#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        q = deque()
        max_len = 0
        for char in s:
            while char in q:
                q.popleft()
            q.append(char)
            max_len = max(max_len, len(q))
        return max_len


# @lc code=end
