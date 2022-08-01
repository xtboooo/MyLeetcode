#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
# Definition for a Node.


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 层序遍历
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         import collections
#         if not root:
#             return root
#         q = collections.deque([root])
#         while q:
#             size = len(q)
#             for i in range(size):
#                 node = q.popleft()
#                 if i < size-1:
#                     node.next = q[0]
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#         return root


# 使用已建立的 \text{next}next 指针
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        curr = root
        while curr:
            dummy_head = Node(-1)  # 为下一行的之前的节点，相当于下一行所有节点链表的头结点；
            pre = dummy_head
            while curr:
                if curr.left:
                    pre.next = curr.left  # 链接下一行的节点
                    pre = curr.left
                if curr.right:
                    pre.next = curr.right
                    pre = curr.right
                curr = curr.next
            curr = dummy_head.next  # 此处为换行操作，更新到下一行
        return root


# @lc code=end
