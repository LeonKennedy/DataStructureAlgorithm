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
        return fr"value:{self.value}, point:{id(self.point)}"

class LinkedList:

    def __init__(self):
        self._sential = Node(None,None)
        #assert(self._tail == Node(None, None))
        self._tail = self._head = Node(None, self._sential)
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

    def pop(self, value = None):
        if self._tail == self._head:
            raise ValueError('empyt link')
        if value is None:
            self._head.point = self._head.point.point
            self._len -= 1
        else:
            cursor = self._head
            while cursor.point != self._sential:
                if cursor.point.value == value:
                    cursor.point = cursor.point.point
                    self._len -= 1
                    return 
                cursor = cursor.point

            raise ValueError(f'value({value}) not found')


    def lpush(self, value):
        new_node = Node(value, self._head.point)
        self._head.point = new_node
        self._len += 1
        
    def rpush(self, value):
        new_node = Node(value, self._tail.point) 
        self._tail.point = new_node
        self._tail = new_node
        self._len += 1


def test():
    link = LinkedList()
    link.rpush(3)
    link.rpush(5)
    print(link)
    print('after   rpush(7) lpush(4):')
    link.rpush(7)
    link.lpush(4)
    print(link)
    print('after   pop():')
    link.pop()
    print(link)
    print('after   pop(7):')
    link.pop(7)
    print(link)

    
if __name__ == "__main__":
    test()



