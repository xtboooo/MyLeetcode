#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start

# 右移计数
class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        n, count = x ^ y, 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count


# Brian Kernighan法
class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        n, count = x ^ y, 0
        while n:
            count += 1
            n &= n - 1
        return count


# 内置
class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


# @lc code=end
