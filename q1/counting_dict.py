#!/usr/bin/env python
"""
Q1 python sample.

@author: FATESAIKOU
@argv[1]: text file
@argv[2]: dic file
@argv[3]: res file
"""

import sys
import re

def createDic(dic_content):
    words = str.splitlines(dic_content)

    return {w: 0 for w in words if len(w) > 0}


def main():
    TXT = sys.argv[1]
    DIC = sys.argv[2]
    RES = sys.argv[3]

    # dic init
    print "[Info] Dict Init"
    dic_src = open(DIC, 'r')
    dic_content = dic_src.read()
    dic_src.close()

    dic = createDic(dic_content)

    # txt read
    print "[Info] Txt read"
    txt_src = open(TXT, 'r')
    txt_content = txt_src.read()
    txt_src.close()

    # get words
    print "[Info] Word extract"
    txt_content = txt_content.replace('\n', ' ')
    txt_words = re.split(r'[^\w]', txt_content)

    # counting
    print "[Info] Word counting"
    dw = set(dic.keys())
    for tw in txt_words:
        if tw in dw:
            dic[tw] += 1

    # get max
    print "[Info] Get max"
    max_key = max(dic, key=dic.get)
    max_val = dic[max_key]

    # get all max
    print "[Info] Get all max"
    words = [(w, max_val) for w in dw if dic[w] == max_val]
    words.sort(key=lambda w: w[0])

    # print result
    print "[Info] Print result"
    s = ''
    for w in words:
        s += str(w[0]) + ' ' + str(w[1]) + '\n'

    dst = open(RES, 'w')
    dst.write(s)
    dst.close()


if __name__ == "__main__":
    main()

