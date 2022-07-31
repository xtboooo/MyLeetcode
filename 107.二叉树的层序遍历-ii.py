#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
class Solution1:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections

        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                curr = q.popleft()
                if not curr:
                    continue
                level.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            if level:
                res.append(level)
        return res[::-1]


# dfs
class Solution2:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        res = []
        dfs(root, 0)
        return res[::-1]


# @lc code=end
