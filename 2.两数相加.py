#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0
    ) -> Optional[ListNode]:
        n1, n2 = l1.val if l1 else 0, l2.val if l2 else 0
        s = n1 + n2 + carry
        value, carry = s % 10, 1 if s > 9 else 0
        next1, next2 = l1.next if l1 else None, l2.next if l2 else None
        if next1 or next2 or carry:
            return ListNode(value, self.addTwoNumbers(next1, next2, carry))
        return ListNode(value)


# @lc code=end
