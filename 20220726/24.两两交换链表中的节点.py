#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 迭代
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head


# 递归
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        tmp = dummy
        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1
        return dummy.next


# @lc code=end
