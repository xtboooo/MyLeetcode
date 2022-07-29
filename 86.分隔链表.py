#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# 将原始链表拆大小链表, 在进行合并
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
        self, head: Optional[ListNode], x: int
    ) -> Optional[ListNode]:
        p = more = ListNode()
        q = less = ListNode()
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        more.next = None
        less.next = p.next
        return q.next


# @lc code=end
