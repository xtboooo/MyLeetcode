#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

示例 1：

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]
示例 2：

输入：nums = [1,2,3,4]
输出：2
示例 3：

输入：nums = [1,1,1,1]
输出：0
"""
from typing import List


# 排序
class Solution1:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res, start = 0, 0
        for end in range(len(nums)):
            while nums[end] - nums[start] > 1:
                start += 1
            if nums[end] - nums[start] == 1:
                res = max(res, end - start + 1)
        return res


# 哈希表
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        import collections

        c = collections.Counter(nums)
        return max(
            (value + c[key + 1] for key, value in c.items() if key + 1 in c),
            default=0,
        )


# @lc code=end
