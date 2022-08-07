#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


# inorder 递归
class Solution1:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        base = None
        max_count = 0
        count = 0

        def update(val):
            nonlocal ans, base, max_count, count
            if val == base:
                count += 1
            else:
                base = val
                count = 1
            if count == max_count:
                ans.append(val)
            elif count > max_count:
                max_count = count
                ans.clear()
                ans.append(val)

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            update(root.val)
            inorder(root.right)

        inorder(root)
        return ans


# bfs 迭代
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        import collections

        q = collections.deque([root])
        ans = []
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        tmp = collections.Counter(res).most_common()
        for k, v in tmp:
            if v == tmp[0][1]:
                ans.append(k)
        return ans


# @lc code=end
