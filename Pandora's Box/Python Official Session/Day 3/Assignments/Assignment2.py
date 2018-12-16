#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:52:01 2018

@author: jmat
"""


def str_cnt(string, ch, start_pos=0, end_pos=-1 ):
    cur_pos=start_pos
    cnt=0
    if end_pos == -1 :
        end_pos=len(string)

    while True:
        cur_pos=string.find(ch,cur_pos,end_pos)
       # print(cur_pos)
        if cur_pos == -1:
            break
        else:
            cnt+=1
        cur_pos+=1
    print("No of occurences of",ch,"in ", string," with start pos",
          start_pos," and end position",end_pos," is "  ,cnt)

str_cnt('phphp','hp',1,3)
#print ( str_cnt('php','p'))
#print("phphp".count("hp",1,3))
