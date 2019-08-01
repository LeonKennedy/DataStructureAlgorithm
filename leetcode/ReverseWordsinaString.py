#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ReverseWordsinaString.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: https://leetcode.com/problems/reverse-words-in-a-string/
# @Create: 2019-08-01 10:37
# @Last Modified: 2019-08-01 10:37


class Solution:
    def reverseWords(self, s: str) -> str:
        j = len(s)-1
        output = list()
        while j >= 0:
            if s[j] == ' ':
                j -= 1
            else:
                i = j
                while i >= 0:
                    if s[i] == ' ':
                        break
                    else:
                        i -= 1
                output.append(s[i + 1:j + 1])
                j = i - 1
        return ' '.join(output)


if __name__ == '__main__':
    s = Solution()
    text1 = "  hello world!  "
    text2 = "the sky is blue"
    s.reverseWords(text2)
