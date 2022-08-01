#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
# Definition for a Node.


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
