#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 中序遍历 递归
class Solution1:
    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        min_value = float("inf")
        self.inorder(root, res)
        for i in range(len(res) - 1):
            min_value = min(min_value, res[i + 1] - res[i])
        return min_value


# 中序遍历 迭代
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        min_value = float("inf")
        pre = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                cur = stack.pop()
                if pre:
                    min_value = min(min_value, cur.val - pre.val)
                pre = cur
                root = cur.right
        return min_value


# @lc code=end
