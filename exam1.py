#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/9/20 19:56
author:    peak
description:
    有一个分布式服务集群，集群内含有N个服务节点，分别记为1到N。
    基于一个列表times，表示消息从两个节点间有向传递需要的时间。times[i]=(s,d,t),其中s 表示
    发出消息的源节点，d表示接收到消息的目标节点，t表示信息的有向传递的时间。
    现在K节点发送了一个信号，请问至少需要多少秒才能使所有的服务节点都接收到该消息？如果消息
    不能传递给集群内全部节点，则返回-1。

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
