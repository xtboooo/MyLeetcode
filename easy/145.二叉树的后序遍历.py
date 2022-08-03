#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res


# 迭代
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                if root.left:
                    root = root.left
                else:
                    root = root.right
            curr = stack.pop()
            res.append(curr.val)
            if stack and stack[-1].left == curr:
                root = stack[-1].right
            else:
                root = None
        return res


# @lc code=end
