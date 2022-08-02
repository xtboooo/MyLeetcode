#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
"""
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
"""


# 递归快速幂
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        def quick_mul(N):
            if N == 0:
                return 1.0
            y = quick_mul(N // 2)
            return y * y if not N % 2 else y * y * x

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)


# 迭代快速幂
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def quick_mul(N):
            ans = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                N //= 2
            return ans

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)


# @lc code=end
