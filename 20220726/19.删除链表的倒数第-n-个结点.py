#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 计算链表的长度
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def get_length(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        # 哑节点
        dummy = ListNode(0, head)
        length = get_length(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


# 栈
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = []
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for _ in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next


# 双指针
class Solution3:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


# @lc code=end
