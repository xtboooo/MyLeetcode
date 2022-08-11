#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start


# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


# 递归
class Solution1:
    def preorder(self, root: "Node") -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return ans


# 迭代
class Solution2:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(reversed(node.children))
        return ans


# @lc code=end
