#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
"""
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

示例 1：

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
示例 2：

输入：root = [1]
输出：["1"]
"""
# Definition for a binary tree node.
from socket import PACKET_OTHERHOST
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution1:
    """
    T(n) =O(n**2)
    S(n) = O(n**2)
    """

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def construct_paths(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
            path += "->"
            construct_paths(root.left, path)
            construct_paths(root.right, path)

        construct_paths(root, "")
        return res


# bfs
class Solution:
    """
    T(n) =O(n**2)
    S(n) = O(n**2)
    """

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        import collections

        paths = []
        if not root:
            return paths
        q_node = collections.deque([root])
        q_path = collections.deque([str(root.val)])
        while q_node:
            node, path = q_node.popleft(), q_path.popleft()
            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    q_node.append(node.left)
                    q_path.append(path + "->" + str(node.left.val))
                if node.right:
                    q_node.append(node.right)
                    q_path.append(path + "->" + str(node.right.val))
        return paths


# @lc code=end
