#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper((root))


# 中序遍历
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        pre = float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre >= root.val:
                return False
            pre = root.val
            root = root.right
        return True


# @lc code=end
