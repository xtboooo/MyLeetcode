#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
# 哈希表
class Solution1:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n:
                n, digit = divmod(n, 10)
                res += digit**2
            return res

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# 哈希表
class Solution2:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n:
                n, digit = divmod(n, 10)
                res += digit**2
            return res

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# 快慢指针
class Solution3:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n:
                n, digit = divmod(n, 10)
                res += digit**2
            return res

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and fast_runner != slow_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


# 数学
# 快慢指针
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n:
                n, digit = divmod(n, 10)
                res += digit**2
            return res

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
        while n != 1 and n not in cycle_members:
            cycle_members.add(n)
            n = get_next(n)
        return n == 1


# @lc code=end
