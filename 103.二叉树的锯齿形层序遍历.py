#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 102写法
class Solution1:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections

        q = collections.deque([root])
        res = []
        f = 0
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
                if f % 2 == 0:
                    res.append(level)
                else:
                    res.append(level[::-1])
            f += 1
        return res


# 双端队列
class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections

        q = collections.deque([root])
        res = []
        f = True
        while q:
            tmp = collections.deque([])
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                if f:
                    tmp.append(curr.val)
                else:
                    tmp.appendleft(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            f = not f
            if tmp:
                res.append(list(tmp))
        return res


# # dfs
class Solution3:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections

        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append(collections.deque())
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        res = []
        dfs(root, 0)
        return list(map(list, res))


# @lc code=end
