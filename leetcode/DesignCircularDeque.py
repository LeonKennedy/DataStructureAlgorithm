#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: DesignCircularDeque.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-22 17:38
# @Last Modified: 2019-07-22 17:38


class Node:
    __slots__ = '_val', '_next'

    def __init__(self, val, node):
        self._val = val
        self._next = node


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._capacity = k
        self._size = 0
        self._tail = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self._size == 0:
            self._tail = Node(value, None)
            self._tail._next = self._tail
        elif self._size == self._capacity:
            return False
        else:
            self._tail._next = Node(value, self._tail._next)
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self._size == 0:
            self._tail = Node(value, None)
            self._tail._next = self._tail
        elif self._size == self._capacity:
            return False
        else:
            self._tail._next = Node(value, self._tail._next)
            self._tail = self._tail._next
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self._size == 1:
            self._tail = None
        elif self._size == 0:
            return False
        else:
            self._tail._next = self._tail._next._next
        self._size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self._size == 1:
            self._tail = None
        elif self._size == 0:
            return False
        else:
            p = self._tail._next
            while p._next is not self._tail:
                p = p._next
            p._next = self._tail._next
            self._tail = p
        self._size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self._tail._next._val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self._tail._val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == self._capacity

def test():
    # [
    #  "deleteLast", "getRear"]
    # [      [], []]
    # [   true, 0]
    circularDeque = MyCircularDeque(5)
    assert circularDeque.insertFront(7)
    assert circularDeque.insertLast(0)
    assert circularDeque.getFront() == 7
    assert circularDeque.insertLast(3)
    assert circularDeque.getFront() == 7
    assert circularDeque.insertFront(9)
    assert circularDeque.getRear() == 3
    assert circularDeque.getFront() == 9
    assert circularDeque.getFront() == 9
    assert circularDeque.deleteLast()
    assert circularDeque.getRear() == 0


if __name__ == '__main__':
    circularDeque = MyCircularDeque(3)
    assert circularDeque.insertLast(1)
    assert circularDeque.insertLast(2)
    assert circularDeque.insertFront(3)
    assert circularDeque.insertFront(4) == False
    assert circularDeque.getRear() == 2
    assert circularDeque.isFull()
    assert circularDeque.deleteLast()
    assert circularDeque.insertFront(4)
    assert circularDeque.getFront() == 4
    test()
    print('Success')