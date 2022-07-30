#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # 深度优先遍历 dfs
class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right
            )


# 广度优先遍历 bfs
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        import collections

        if not p and not q:
            return True
        if not p or not q:
            return False
        q1 = collections.deque([p])
        q2 = collections.deque([q])
        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if n1.val != n2.val:
                return False
            l1, r1 = n1.left, n1.right
            l2, r2 = n2.left, n2.right
            if (not l1) ^ (not l2):
                return False
            if (not r1) ^ (not r2):
                return False
            if l1:
                q1.append(l1)
            if r1:
                q1.append(r1)
            if l2:
                q2.append(l2)
            if r1:
                q2.append(r2)
        return not q1 and not q2


# @lc code=end
