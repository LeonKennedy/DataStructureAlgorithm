#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: BagofTokens.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-09-11 19:47
# @Last Modified: 2019-09-11 19:47
from collections import deque
from typing import List


class Solution:
    max = 0
    score = 0
    dq = None
    power = 0

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        self.score = self.max = 0
        tokens.sort()
        self.dq = deque(tokens)
        self.power = P
        #
        while self.dq:
            if self.power >= self.dq[0]:
                self.face_up(self.dq[0])
            else:
                if self.score > 0:
                    self.face_down(self.dq[-1])
                else:
                    return self.max
        return self.max

    def face_up(self, token):
        self.dq.remove(token)
        self.power -= token
        self.score += 1
        if self.score > self.max:
            self.max = self.score

    def face_down(self, token):
        self.dq.remove(token)
        self.power += token
        self.score -= 1


def test():
    a = Solution()
    tokens, P = [100], 50
    assert 0 == a.bagOfTokensScore(tokens, P)
    tokens, P = [100, 200], 150
    assert 1 == a.bagOfTokensScore(tokens, P)
    tokens, P = [100, 200, 300, 400], 200
    assert 2 == a.bagOfTokensScore(tokens, P)
    tokens, P = [81, 91, 31], 73
    assert 1 == a.bagOfTokensScore(tokens, P)


if __name__ == '__main__':
    test()
