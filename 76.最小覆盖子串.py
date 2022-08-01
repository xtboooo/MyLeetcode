#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
"""
Hard

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""


# 滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        need_cnt = len(t)
        i = 0
        res = (0, float("inf"))
        for j, c in enumerate(s):
            if need[c] > 0:
                need_cnt -= 1
            need[c] -= 1
            if need_cnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c1 = s[i]
                    if need[c1] == 0:
                        break
                    need[c1] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                need_cnt += 1
                i += 1
        return "" if res[1] > len(s) else s[res[0] : res[1] + 1]


# @lc code=end
