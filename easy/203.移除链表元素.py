#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 递归
class Solution1:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        if not head:
            return
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


# 迭代
class Solution2:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        # 需要先保证头结点的位置
        while head and head.val == val:
            head = head.next
        if not head:
            return
        pre = head
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


# 哨兵
class Solution3:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


# 双指针
class Solution4:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        pre, curr = head, head
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre.next = curr.next
            curr = curr.next
        return head


# @lc code=end
