#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
# Definition for a Node.
"""
Medium

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

示例 1：

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
示例 2:

输入：root = []
输出：[]
"""


from typing import Optional


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 层序遍历
class Solution1:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        import collections

        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


# 使用已建立的 \text{next}next 指针
class Solution2:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # 层内移动
                head.left.next = head.right
                if head.next:  # 通过已经建立的next, 实现不同不节点的子节点连接
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left  # 向下层移动
        return root


# @lc code=end
