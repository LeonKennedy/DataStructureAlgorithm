#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: SkipList.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-11 17:33
# @Last Modified: 2019-08-11 17:33

import random

class Item:
    __slots__ = "val", "next", "below"

    def __init__(self, val):
        self.val = val
        self.next = None
        self.below = None


class SkipList:

    def __init__(self):
        self._head = self._new_layer()

    def show(self):
        p = self._head
        while p is not None:
            r = p.next
            while not isinstance(r.val, Infinity):
                print(r.val, end=' ')
                r = r.next
            print()
            p = p.below

    def _new_layer(self):
        negative_infinity = Item(NeInfinity())
        infinity = Item(Infinity())
        negative_infinity.next = infinity
        return negative_infinity

    def _add_new_layer(self):
        n = self._new_layer()
        n.below = self._head
        self._head = n

    def insert(self, key):
        q = self._insert_below(self._head, key)
        if q is not None:
            self._add_new_layer()
            self._insert_after(self._head, q, key)

    def _insert_below(self, p, key):
        while p.next is not None and p.next.val < key:
            p = p.next

        if p.below is None:
            return self._insert_after(p, None, key)
        else:
            q = self._insert_below(p.below, key)
            return q if q is None else self._insert_after(p, q, key)

    def _insert_after(self, p, q, key):
        new_item = Item(key)
        new_item.next = p.next
        new_item.below = q
        p.next = new_item
        if new_item.next.val == key:
            return None
        return random.choice([new_item, None])

    def search(self, key):
        p = self._head
        while p is not None:

            while p.val < key and p.next.val < key:
                p = p.next

            if p.val == key:
                return True
            else:
                p = p.below

        raise ValueError(f"Key({key}) not found")

    def remove(self, key):
        pass

    def __iter__(self):
        pass

    def find_by_position(self, p):
        pass

    def access_by_position(self, p):
        pass

    def delete_by_position(self, p):
        pass


class Infinity:

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return True

    def __eq__(self, other):
        return False


class NeInfinity:

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return False

    def __eq__(self, other):
        return False


if __name__ == '__main__':
    s = SkipList()
    for i in random.choices(range(9999), k = 1000 ):
        s.insert(i)
    s.show()
    s.search(29)