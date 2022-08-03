#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# 排序
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if i + 2 <= len(nums) and nums[i] == nums[i + 1]:
                return True
        return False


# 哈希表
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        import collections

        hash_map = collections.defaultdict(int)
        for num in nums:
            hash_map[num] += 1
            if hash_map[num] > 1:
                return True
        return False


# @lc code=end
