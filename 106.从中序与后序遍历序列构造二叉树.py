#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)
        root.left = self.buildTree(
            inorder[:root_index], postorder[:root_index]
        )
        root.right = self.buildTree(
            inorder[root_index + 1 :], postorder[root_index:-1]
        )  # -1排除根节点
        return root


# @lc code=end
