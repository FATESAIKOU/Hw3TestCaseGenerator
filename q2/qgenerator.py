#!/usr/bin/env python
"""
Q2 question & answer generator

@author: FATESAIKOU
@argv[1]: dic file
@argv[2]: question input sequence
@argv[3]: question answer
"""

import BST

import sys
import random
import copy
import numpy as np


def getNorm(mu, sigma):
    return round(np.rando.normal(mu, sigma, 1)[0])


def main():
    DIC = sys.argv[1]
    SEQ = sys.argv[2]
    ANS = sys.argv[3]
    
    # load dic
    dic_src = open(DIC, 'r')
    words = str.splitlines(dic_src.read())
    dic_src.close()

    # set max total count
    total_count = random.randint(10, 1000)

    # select candidate words
    mu = 10
    sigma = 3
    cand_num = total_count / mu
    cand_words = random.sample(words, cand_num)

    # set words distribution
    now_count = 0
    word_dist = {w: 0 for w in cand_words}

    while now_count < total_count:
        w = random.choice(cand_words)
        c = getNorm(mu, sigma)
        
        word_dist[w] += c
        now_count += c

    # create seq
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
            
    # dump seq & bst(answer)
    seq_src = open(SEQ, 'w')
    seq_src.write('\n'.join(seq) + '\n')
    seq_src.close()


if __name__ == "__main__":
    main()
