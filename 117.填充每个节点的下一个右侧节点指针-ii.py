#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
# Definition for a Node.
"""
Medium

给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
"""


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
class Solution1:
    def connect(self, root: "Node") -> "Node":
        import collections

        if not root:
            return root
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
