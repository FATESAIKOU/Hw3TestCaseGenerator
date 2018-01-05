#!/usr/bin/env python
"""
Q3 question & answer generator

@author: FATESAIKOU
@argv[1]: dic file
@argv[2]: place num
@argv[3]: connectivity
@argv[4]: question input sequence
@argv[5]: answer file
"""

import sys
import random
import numpy as np

from pprint import pprint

def main():
    DIC = sys.argv[1]
    PLM = int(sys.argv[2])
    CON = int(sys.argv[3])
    SEQ = sys.argv[4]
    ANS = sys.argv[5]

    # load dic
    print "[Info] Dict load"
    dic_src = open(DIC, 'r')
    place = str.splitlines(dic_src.read())
    dic_src.close()

    # select candidate place
    print "[Info] Select candidate place"
    cand_place = random.sample(place, PLM)

    # generate paths
    print "[Info] Generate paths"
    paths = []
    for i in xrange(len(cand_place)):
        for j in xrange(i, len(cand_place)):
            if (i == j):
                continue
            r = random.randint(0, random.randint(1, CON))

            if (r != 0):
                paths.append( (cand_place[i], cand_place[j], random.randint(1, 10)) );
    random.shuffle(paths)

    # rebuild array
    print "[Info] Rebuild array from sequence"
    array = np.zeros((PLM, PLM), dtype=np.int32)
    array.fill(-1)
    for i in xrange(PLM):
        array[i, i] = 0
    
    appear_seq = []
    for p in paths:
        for ps in p[0:2]:
            if ps not in appear_seq:
                appear_seq.append(ps)

        idx_a = appear_seq.index(p[0])
        idx_b = appear_seq.index(p[1])

        array[idx_a, idx_b] = p[2]
        array[idx_b, idx_a] = p[2]

    
    real_size = len(appear_seq)
    array = array[0:real_size, 0:real_size]
    print "[Info] ori path"
    pprint(array)

    # generate answer
    print "[Info] Generator answer"
    for k in xrange(real_size):
        for i in xrange(real_size):
            for j in xrange(real_size):
                if array[i, k] != -1 and array[k, j] != -1 and \
                    (array[i, k] + array[k, j] < array[i, j]):
                    array[i, j] = array[i, k] + array[k, j]
    
    print "[Info] Shortest path"
    pprint(array)

    # dump input sequence & answer
    print "[Info] Dump sequences"
    s = ''
    for p in paths:
        s += p[0] + ' ' + str(p[2]) + ' ' + p[1] + '\n'

    src = open(SEQ, 'w')
    src.write(s)
    src.close()

    print "[Info] Dump answer"
    s = ''
    for i in xrange(real_size):
        for j in xrange(real_size):
            s += str(array[i, j]) if array[i, j] != -1 else 'inf'
            s += ' '

        s += '\n'

    src = open(ANS, 'w')
    src.write(s)
    src.close()


if __name__ == "__main__":
    main()
