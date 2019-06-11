#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: RemoveNthEndNode.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:
# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#   Given n will always be valid.
#
# @Create: 2019-06-11 17:26
# @Last Modified: 2019-06-11 17:26


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head





def test():
    head = ListNode(None)
    for i in range(5, 0, -1):
        temp_node = ListNode(i)
        temp_node.next = head.next
        head.next = temp_node
    return head.next


def show(head):
    temp = head
    print('\n', head.val, end='')
    while temp.next is not None:
        temp = temp.next
        print('->', temp.val, end='')


if __name__ == "__main__":
    c = test()
    show(c)
    s = Solution()
    d = s.remove_nth_from_end(c, 5)

    show(d)

