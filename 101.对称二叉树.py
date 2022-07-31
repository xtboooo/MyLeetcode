#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return check(left.left, right.right) and check(
                left.right, right.left
            )

        if root is None:
            return True
        return check(root.left, root.right)


# 迭代
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        import collections

        if root is None or (root.left is None and root.right is None):
            return True
        q = collections.deque()
        q.append((root.left, root.right))
        while q:
            left, right = q.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        return True


# @lc code=end
