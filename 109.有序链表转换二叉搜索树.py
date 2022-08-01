#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 分治
class Solution1:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_mid(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build_tree(left, right):
            if left == right:
                return None
            mid = get_mid(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root

        return build_tree(head, None)


# 分治+中序遍历优化
class Solution2:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        def build_tree(left, right):
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = build_tree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = build_tree(mid + 1, right)
            return root

        return build_tree(0, get_length(head) - 1)


# @lc code=end
