#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution1:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        def dfs(root, targetSum):  # root需要原地引用root, 否则将超过最大递归深度
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val  # 动态改变目标值
            if (
                not root.left and not root.right and targetSum == 0
            ):  # 叶子节点且与目标值匹配
                res.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()  # 还原

        res = []
        path = []
        dfs(root, targetSum)
        return res


# bfs
class Solution2:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        import collections

        q = collections.deque([(root, [], 0)])
        res = []
        while q:
            node, path, total_sum = q.popleft()
            if not node:
                continue
            if (
                not node.left
                and not node.right
                and node.val + total_sum == targetSum
            ):
                res.append(path + [node.val])
            q.append((node.left, path + [node.val], total_sum + node.val))
            q.append((node.right, path + [node.val], total_sum + node.val))
        return res


# @lc code=end
