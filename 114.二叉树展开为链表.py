#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 先前序遍历(递归) 后展开
class Solution1:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_order_list = []

        def preorder_traversal(root):
            if root:
                pre_order_list.append(root)
                preorder_traversal(root.left)
                preorder_traversal(root.right)

        preorder_traversal(root)
        size = len(pre_order_list)
        for i in range(1, size):
            prev, curr = pre_order_list[i - 1], pre_order_list[i]
            prev.left = None
            prev.right = curr


# 先前序遍历(迭代) 后展开
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_order_list = []
        stack = []
        node = root
        while stack or node:
            while node:
                pre_order_list.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        size = len(pre_order_list)
        for i in range(1, size):
            prev, curr = pre_order_list[i - 1], pre_order_list[i]
            prev.left = None
            prev.right = curr


# 遍历展开同时进行
class Solution3:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr


# 寻找前驱节点
class Solution4:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None


# @lc code=end
