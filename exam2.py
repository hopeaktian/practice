#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/9/20 22:17
author:    peak
description:
"""
def turnlist(x):
    if ',' in x:
        x = x.split(',')
        return x
    else:
        x = x.split()
        return x

def exam2():
    L1 = raw_input("N,T:")
    Str = raw_input("string:")
    L1 = turnlist(L1)
    N = L1[0]
    T = int(L1[1])

    for i in range(T):
        L2 = raw_input("type,X:")
        L2 = turnlist(L2)
        X = L2[1]
        X = int(X)
        if L2[0] == "1":
            head = Str[0:-X]
            s1 = Str.replace(head, "")
            S = s1+head
            print S
        else:
            print Str[X]
exam2()