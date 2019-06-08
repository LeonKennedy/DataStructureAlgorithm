#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: linked_list.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2019-06-08 09:57:42
# @Last Modified: 2019-06-08 09:57:42
#

from collections import namedtuple

#Node = namedtuple('node', ['value', 'point'])

class Node:
    def __init__(self, value, point):
        self.value = value
        self.point = point

    def __repr__(self):
        return fr"[Node({id(self)})-({self.value})]"

class LinkedList:

    def __init__(self):
        self._sential = Node(None,None)
        #assert(self._tail == Node(None, None))
        self._head = Node(None, self._sential)
        self._len = 0

    def __len__(self):
        return self._len

    def __str__(self):
        text = '[head]'
        cursor = self._head.point
        while cursor != self._sential:
            text = text + f'->{cursor.value}'
            cursor = cursor.point
        text += f' len({self._len})'
        return text

    def pop(self, value):
        if self._len == 0:
            raise ValueError('empyt link')
        cursor = self._head
        while cursor.point != self._sential:
            if cursor.point.value == value:
                cursor.point = cursor.point.point
                self._len -= 1
                return 
            cursor = cursor.point

        raise ValueError(f'value({value}) not found')


    def push(self, value):
        new_node = Node(value, self._head.point)
        self._head.point = new_node
        self._len += 1
        
    def reverse(self):
        if self._len < 2:
            return 
        new_head = Node(None, self._sential)
        while self._head.point != self._sential:
            cursor = self._head.point
            self._head.point = self._head.point.point
            
            cursor.point = new_head.point
            new_head.point = cursor
        self._head = new_head
    
    def check_circle(self):
        """
        长短指针快慢检查
        """
        fast = slow = slow2 = self._head.point
        while 1:
            if fast.point is None or fast.point.point is None:
                return None, None
            fast = fast.point.point
            slow = slow.point
            if fast == slow:
                cross = slow
                length = 0
                while 1:
                    slow = slow.point
                    length += 1
                    if slow == cross:
                        break
                length -= 1   # 减去哨兵
                while 1:
                    slow2 = slow2.point
                    slow = slow.point
                    if slow2 == slow:
                        return length, slow


def test_linked_list():
    link = LinkedList()
    link.push(3)
    link.push(None)
    link.push(5)
    print(link)
    print('after   rpush(7) lpush(4):')
    link.push(7)
    link.push(4)
    print(link)
    print('after   pop():')
    link.pop(None)
    print(link)
    print('after   pop(7):')
    link.pop(7)
    print(link)
    link.reverse()
    print('after   pop(7):')
    print(link)
    print('after   pop(3) reverse():')
    link.pop(3)
    link.reverse()
    print(link)


def test_check_circle():
    link = LinkedList()
    for i in range(10):
        link.push(i)
    print(f"entrance is {link._head.point}")
    link._sential.point = link._head.point
    for i in range(10, 20):
        link.push(i)
    print(link)
    print('circle length and entrance:')
    print(link.check_circle())



    
if __name__ == "__main__":
    #test_linked_list()
    test_check_circle()



