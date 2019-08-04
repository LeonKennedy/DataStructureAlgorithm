#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: HashMap.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-26 16:49
# @Last Modified: 2019-07-26 16:49

import random
from collections import MutableMapping
from typing import Any, Iterator, _T_co, _KT, _VT_co, _VT


class MapBase(MutableMapping):
    class _Item:
        __slots__ = "_key", "_val"

        def __init__(self, k, v):
            self._key = k
            self._val = v

        def __hash__(self):
            return hash((self._key, self._val))


class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if key == item._key:
                return item._val
        raise ValueError(f'Key({key}) Not Found')

    def __setitem__(self, key, value):
        for item in self._table:
            if key == item._val:
                return
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        for item in self._table:
            if key == item._key:
                break
        else:
            raise ValueError(f'Key({key}) Not Found')
        self._table.remove(item)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __len__(self):
        return len(self._table)

    def __contains__(self, key):
        for item in self._table:
            if key == item._key:
                return True
        return False


class HashMapBase(MapBase):

    def __len__(self) -> int:
        return self._len

    def __init__(self, capacity=8):
        self._c = capacity
        self._len = 0
        self._bucket = capacity * [None]

    @property
    def _ru(self):
        return self._len / self._c

    def _hash_func(self, key) -> int:
        return self._zip(self._hash_key(key))

    def _hash_key(self, key: Any) -> int:
        return hash(key)

    def _zip(self, hash_code: int) -> int:
        return hash_code % self._c


class ChainHashMap(HashMapBase):
    """
    使用链表存储
    """
    def __iter__(self) -> Iterator:
        for bucket in self._bucket:
            if bucket is not None:
                yield from bucket

    def __delitem__(self, key) -> None:
        index = self._hash_func(key)
        if self._bucket[index]:
            if key in self._bucket[index]:
                del self._bucket[index][key]
                self._len -= 1
            else:
                raise ValueError(f"key({key}) not found")
        else:
            raise ValueError(f"key({key}) not found")

    def __getitem__(self, key) -> HashMapBase._Item:
        index = self._hash_func(key)
        if self._bucket[index]:
            return self._bucket[index][key]
        else:
            raise ValueError(f"key({key}) not found")

    def __setitem__(self, key, value):
        index = self._hash_func(key)
        if self._bucket[index]:
            if key in self._bucket[index]:
                return
            else:
                self._bucket[index][key] = value
                self._len += 1
        else:
            self._bucket[index] = UnsortedTableMap()
            self._bucket[index][key] = value
            self._len += 1


class ProbeHashMap(HashMapBase):
    """
    使用随机探测
    """
    _sentienl = object()
    def __init__(self, capacity=7, p=109345121):
        super(ProbeHashMap, self).__init__(capacity)
        e = list(range(1, capacity + 1))
        random.shuffle(e)
        self.random_list = e
        self.p = p   # MAD
        self.max_random = 0

    def is_available(self, j):
        return self._bucket[j] is None or self._bucket[j] is self._sentienl

    def _find_slot(self, k):
        for i, j in enumerate(self._hash_func(k)):
            if self.is_available(j):
                first = j
            if self._bucket[j] is None:
                return False, first
            if self._bucket[j] is self._sentienl:
                pass
            else:
                if self._bucket[j]._key == k:
                    return True, j
        raise ValueError(f"not found")

    def __setitem__(self, k, v) -> None:
        if self._ru > 2/3:
            self._resize()
        exsist, index = self._find_slot(k)
        if exsist:
            self._bucket[index] = self._Item(k, v)
        else:
            self._bucket[index] = self._Item(k, v)
            self._len += 1

    def __delitem__(self, key) -> None:
        exsist, index = self._find_slot(key)
        if exsist:
            del self._bucket[index]
            self._len -= 1
        else:
            raise IndexError(f"key({key}) not found")

    def __getitem__(self, key):
        exsist, index = self._find_slot(key)
        if exsist:
            return self._bucket[index]._val
        else:
            raise IndexError(f"key({key}) not found")

    def __iter__(self) -> Iterator:
        for item in self._bucket:
            if item is not None and item is not self._sentienl:
                yield item._key

    def _resize(self):
        self._c *= 2
        old_buckets = self._bucket
        self._bucket = self._c * [None]
        for item in old_buckets:
            if item is not None and item is not self._sentienl:
                self[item._key] = item._val

    def _hash_func(self, key) -> int:
        hash_code = self._hash_key(key)
        yield from self._zip(hash_code)

    def _zip(self, hash_code: int) -> int:
        num = 0
        for c in [0, *self.random_list]:
            num += 1
            self.max_random = max(self.max_random, num)
            yield (hash_code + c) % self.p % self._c


class SortedTableMap(MapBase):

    def __setitem__(self, k: _KT, v: _VT) -> None:
        index = self._find_index(k, 0, len(self._table))
        if index < 0:
            self._table.insert(index, self._Item(k, v))
        else:
            self._table[index] = self._Item(k,v)

    def __delitem__(self, v: _KT) -> None:
        index = self._find_index(k, 0, len(self._table))
        if index < 0:
            raise IndexError(f"Index({k}) not found!")
        else:
            del self._table[index]

    def __getitem__(self, k: _KT) -> _VT_co:
        index = self._find_index(k, 0, len(self._table)-1)
        if index >= 0:
            return self._table[index]._val
        else:
            raise IndexError(f"Index({k}) not found!")

    def __len__(self) -> int:
        return len(self._table)

    def __iter__(self) -> Iterator[_T_co]:
        for item in self._table:
            yield item._key

    def _find_index(self, k, l, r):
        while l < r:
            mid = r + l >> 1
            if self._table[mid]._key < k:
                l = mid + 1
            elif self._table[mid]._key > k:
                r = mid - 1
            else:
                return mid
        return -1

    def __init__(self):
        self._table = []


if __name__ == '__main__':
    # chm = ChainHashMap(7)
    # for i in range(1, 100):
    #     chm[i] = i
    # print([i for i in chm])
    phm = ProbeHashMap(17)
    for i in range(1, 18):
        phm[i] = i
    phm[18] = 18
    for k,v in phm.items():
        print(v)