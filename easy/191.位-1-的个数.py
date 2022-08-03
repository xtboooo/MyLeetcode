#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
# 循环检查二进制位
class Solution1:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res += n & 1
            n >>= 1
        return res


# 优化
class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


# @lc code=end
