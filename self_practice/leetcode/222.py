# coding: utf-8
# @Author : lryself
# @Date : 2020/11/24 22:23
# @Software: PyCharm

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        from queue import Queue
        if not root:
            return 0
        n = 0
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            n += 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return n
