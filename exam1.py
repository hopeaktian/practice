#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/9/20 19:56
author:    peak
description:
"""

def test():
    times = raw_input("times:")
    N = raw_input("N:")
    K = raw_input("K:")
    ks = []
    alltimes=0

    times = times.replace('[', '')
    times = times.replace(']', '')
    times = times.replace(',', '')

    list=[]

    i = 0
    while i<len(times):
        lis = times[i:i+3]
        li=[]
        for r in lis:
            li.append(int(r))
        list.append(li)
        i+=3

    for j in list:
        if j[0] == int(K):
            ks.append(j)
    if len(ks) < int(N)-1 :
        print '-1'
    else:
        for m in ks:
            alltimes = m[1]+m[2]
        return alltimes
print test()