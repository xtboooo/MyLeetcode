#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        add = n - k % n
        if add == n:
            return head

        # 当前curr为尾节点, 连接头节点成环
        curr.next = head
        while add:
            curr = curr.next
            add -= 1
        # 断开环
        ret = curr.next
        curr.next = None
        return ret


# @lc code=end
