#!/usr/bin/env python
# coding: utf-8

#
# 每辆车最多坐50人，哪两个班坐一辆车最合适？
#

# class and student number map
cla_m = {'1-1':24, '1-2':20, '1-3':22,
         '2-1':30, '2-2':28, '2-3':25}

# sort by their student number (reverse order, big -> small)
clm_sm = sorted(cla_m.iteritems(), key=lambda d:d[1], reverse = True)

#
n = len(clm_sm)
for i in range(n/2):
    c1 = clm_sm[i]
    c2 = clm_sm[n-1-i];

    print('bus[%2d]: class %s and %s' % (i, c1[0], c2[0]))
