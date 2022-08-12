#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

示例 1：

输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]
示例 2：

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 递归
class Solution1:
    def postorder(self, root: "Node") -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return
            for ch in root.children:
                dfs(ch)
            ans.append(root.val)

        dfs(root)
        return ans


# 迭代
class Solution2:
    def postorder(self, root: "Node") -> List[int]:
        if root is None:
            return []
        ans = []
        stack = [root]
        vis = set()
        while stack:
            node = stack[-1]
            if not node.children or node in vis:
                ans.append(node.val)
                stack.pop()
                continue
            stack.extend(reversed(node.children))
            vis.add(node)
        return ans


# @lc code=end
