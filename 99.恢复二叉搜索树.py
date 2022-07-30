#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 显式中序遍历
class Solution1:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ...
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)
        x, y = None, None
        pre = nodes[0]
        for i in range(1, len(nodes)):
            if nodes[i].val < pre.val:
                y = nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        if x and y:
            x.val, y.val = y.val, x.val


# 隐式中序遍历
class Solution2:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ...
        x, y, pre = None, None, None

        def dfs(node):
            nonlocal x, y, pre
            if not node:
                return None
            dfs(node.left)
            if not pre:
                pre = node
            else:
                if pre.val > node.val:
                    y = node
                    if not x:
                        x = pre
                pre = node
            dfs(node.right)

        dfs(root)
        if x and y:
            x.val, y.val = y.val, x.val


# 莫里斯遍历
class Solution3:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ...
        ...


# @lc code=end
