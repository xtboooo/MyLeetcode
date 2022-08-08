#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:
    """
    复杂度分析

    时间复杂度：O(N)O(N)，其中 NN 为二叉树的节点数，即遍历一棵二叉树的时间复杂度，每个结点只被访问一次。

    空间复杂度：O(Height)O(Height)，其中 HeightHeight 为二叉树的高度。由于递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，而递归的深度显然为二叉树的高度，并且每次递归调用的函数里又只用了常数个变量，所以所需空间复杂度为 O(Height)O(Height) 。

    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1

        def depth(root):
            # 访问到空节点了，返回0
            if not root:
                return 0
            # 左儿子为根的子树的深度
            l = depth(root.left)
            # 右儿子为根的子树的深度
            r = depth(root.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, l + r + 1)
            # 返回该节点为根的子树的深度
            return max(l, r) + 1

        depth(root)
        return self.ans - 1


# @lc code=end
