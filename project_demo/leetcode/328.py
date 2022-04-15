# coding: utf-8
# @Author : lryself
# @Date : 2020/11/13 17:17
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        temp = head
        list_head = ListNode()
        list_temp = list_head
        while temp.next is not None:
            if temp.next.next is None:
                list_temp.next = temp.next
                list_temp = list_temp.next
                break
            list_temp.next = temp.next
            temp.next = temp.next.next
            list_temp = list_temp.next
            temp = temp.next
        list_temp.next = None
        temp.next = list_head.next
        return head


if __name__ == '__main__':
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    x = s.oddEvenList(head=l)
    while x is not None:
        print(x.val)
        x = x.next