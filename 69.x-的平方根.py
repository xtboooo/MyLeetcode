#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start

# 内置开方
class Solution1:
    def mySqrt(self, x: int) -> int:
        import math

        return int(math.sqrt(x))


# exp + log
class Solution2:
    def mySqrt(self, x: int) -> int:
        import math

        if x == 0:
            return 0

        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


# 二分法
class Solution3:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# 牛顿逼近 pass
class Solution4:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


# @lc code=end
