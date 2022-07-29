#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        def reverseList(head):
            pre, cur = None, head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        dummy = ListNode(-1, next=head)
        pre = dummy
        # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
        for _ in range(left - 1):
            pre = pre.next
        right_node = pre
        # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
        for _ in range(right - left + 1):
            right_node = right_node.next
        # 第 3 步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next
        # 注意：切断链接
        pre.next = None
        right_node.next = None
        # 第 4 步：同第 206 题，反转链表的子区间
        reverseList(left_node)
        # 第 5 步：接回到原来的链表中
        pre.next = right_node
        left_node.next = curr
        return dummy.next


# @lc code=end
