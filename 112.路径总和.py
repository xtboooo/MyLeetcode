#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(
            root.left, targetSum - root.val
        ) or self.hasPathSum(root.right, targetSum - root.val)


# bfs
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        import collections

        q_node = collections.deque([root])
        q_value = collections.deque([root.val])
        while q_node:
            node = q_node.popleft()
            value = q_value.popleft()
            if not node.left and not node.right:
                if value == targetSum:
                    return True
                continue
            if node.left:
                q_node.append(node.left)
                q_value.append(node.left.val + value)
            if node.right:
                q_node.append(node.right)
                q_value.append(node.right.val + value)
        return False


# @lc code=end
