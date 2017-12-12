#!/usr/bin/env python
"""
Q2 question & answer generator

@author: FATESAIKOU
@argv[1]: dic file
@argv[2]: question input sequence
@argv[3]: question answer
"""

import sys
import random
import copy
import numpy as np


def getNorm(mu, sigma):
    return round(np.random.normal(mu, sigma, 1)[0])


def main():
    DIC = sys.argv[1]
    SEQ = sys.argv[2]
    # ANS = sys.argv[3]
    
    # load dic
    print "[Info] Dict load"
    dic_src = open(DIC, 'r')
    words = str.splitlines(dic_src.read())
    dic_src.close()

    # set max total count
    print "[Info] Total count set"
    total_count = random.randint(10, 1000)

    # select candidate words
    print "[Info] Select candidate words"
    mu = 10
    sigma = 3
    cand_num = total_count / mu
    cand_words = set(random.sample(words, cand_num))

    # set words distribution
    print "[Info] Create words distribution"
    now_count = 0
    word_dist = {w: 0 for w in cand_words}

    while now_count < total_count:
        w = random.sample(cand_words, 1)[0]
        c = int(getNorm(mu, sigma))
        
        word_dist[w] += c
        now_count += c

    for w in list(cand_words):
        if word_dist[w] == 0:
            word_dist.pop(w)
            cand_words.discard(w)
    
    print "[Info] word_count:", now_count

    # create seq
    print "[Info] Create sequence"
    seq = []
    create_dist = {w: 0 for w in cand_words}
    create_words = set(copy.copy(cand_words))

    while len(create_words) != 0:
        w = random.sample(create_words, 1)[0]
        r = random.randint(0, random.randint(1, 3))

        if (r == 0 and create_dist[w] != 0):
            seq.append('-' + w)
            create_dist[w] -= 1
        else:
            seq.append('+' + w)
            create_dist[w] += 1
            
        if (create_dist[w] == word_dist[w]):
            create_dist.pop(w)
            create_words.discard(w)

    # create BST with seq
    print "[Info] Create BST"
            
    # dump seq & bst(answer)
    print "[Info] Dump seq & bst"
    seq_src = open(SEQ, 'w')
    seq_src.write('\n'.join(seq) + '\n')
    seq_src.close()


if __name__ == "__main__":
    main()
