#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution1:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                res.append(root.left.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return sum(res)


# bfs
class Solution2:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        import collections

        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    res.append(node.left.val)
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return sum(res)


# @lc code=end
