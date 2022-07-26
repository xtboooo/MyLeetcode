#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phone_map[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = []
        combinations = []
        backtrack(0)
        return combinations


# @lc code=end
