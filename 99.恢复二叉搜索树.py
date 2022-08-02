#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
"""
Medium

给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。

示例 1：

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
示例 2：

输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
"""
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
