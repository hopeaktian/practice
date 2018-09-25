#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/9/20 22:17
author:    peak
description:
    小明同学需要对一个长度为N的字符串进行处理，他需要按照要求执行若干步骤，每个步骤都均为下面
    2种操作中的一种，2种操作如下：
    TYPE1. 从字符串结尾开始算起，将第X个字符之前的字符移动到字符串末尾
    TYPE2. 输出字符串索引为X的字符串
    帮小明解决问题。

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
