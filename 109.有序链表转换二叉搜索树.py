#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start

"""
Medium

给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。

示例 1:

输入: head = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
示例 2:

输入: head = []
输出: []
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for singly-linked list.
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
