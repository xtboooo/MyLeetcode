#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List


# 完整构建
class Solution1:
    """
    T(n) = O(n**2)
    S(n) = O(n**2)
    """

    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(row)
        return res[rowIndex]


# 2d dp
class Solution2:
    """
    T(n) = O(n**2)
    S(n) = O(n*(n+1)/2)
    """

    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1 for _ in range(i + 1)] for i in range(rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[-1]


# # 1d dp
class Solution3:
    """
    T(n) = O(n**2)
    S(n) = O(n)
    """

    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            # 为啥不从左向右遍历呢？因为如果从左向右遍历，那么左边的元素已经更新为第 i 行的元素了，而右边的元素需要的是第 i - 1i−1 行的元素。故从左向右遍历会破坏元素的状态。
            for j in range(i - 1, 0, -1):
                dp[j] += dp[j - 1]
        return dp[-1]


# @lc code=end
