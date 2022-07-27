#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord("a")] += 1
            res[tuple(counts)].append(word)
        return list(res.values())


# @lc code=end
