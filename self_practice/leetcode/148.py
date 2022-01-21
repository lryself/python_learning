# coding: utf-8
# @Author : lryself
# @Date : 2020/11/21 14:10
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        intlist = []
        while head is not None:
            intlist.append(head.val)
            head = head.next
        intlist.sort()
        result = ListNode()
        p = result
        for i in intlist:
            p.next = ListNode(i, None)
            p = p.next
        return result.next


if __name__ == '__main__':
    s = Solution()
    result = s.sortList(ListNode(4, ListNode(1, ListNode(2, ListNode(3)))))
    while result is not None:
        print(result.val)
        result = result.next
