#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    T(n) = O(n)
    S(n) = O(n)
    """

    def __init__(self) -> None:
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_max_gain(node):
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            price_new_path = node.val + left_gain + right_gain
            # 更新答案
            self.max_sum = max(self.max_sum, price_new_path)
            # 返回节点的最大贡献值
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_sum


# @lc code=end
