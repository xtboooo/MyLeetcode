#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
"""
Easy

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            res.append(curr.val)
            dfs(curr.right)

        res = []
        dfs(root)
        return res


# 迭代
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


# 标记法
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(0, root)]
        while stack:
            flag, curr = stack.pop()
            if not curr:
                continue
            if flag == 0:
                stack.append((0, curr.right))
                stack.append((1, curr))
                stack.append((0, curr.left))
            else:
                res.append(curr.val)
        return res


# @lc code=end
