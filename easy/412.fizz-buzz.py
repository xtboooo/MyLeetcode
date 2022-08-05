#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
from typing import List


class Solution:
    """
    T(n) = O(n)
    S(n) = O(1)
    """

    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            fizz, buzz = i % 3 == 0, i % 5 == 0
            if fizz and buzz:
                res.append("FizzBuzz")
            elif fizz:
                res.append("Fizz")
            elif buzz:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


# @lc code=end
