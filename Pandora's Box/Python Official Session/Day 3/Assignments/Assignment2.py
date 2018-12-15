#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:52:01 2018

@author: jmat
"""


def str_cnt(string, ch, start_pos=0, end_pos=-1 ):
    cur_pos=start_pos
    cnt=0
    end_pos = len(string) if end_pos== -1 else end_pos
    #print(string[end_pos])
    print(string[cur_pos:end_pos])
    for i in string[cur_pos:end_pos]:
        print(i)
        print (cur_pos)
        print(string[cur_pos:end_pos] )
        print(cnt, "\n")
        cur_pos+=1
        #cur_pos=string[cur_pos:end_pos].find(ch)+1 
        cnt+=1
    return cnt

print ( str_cnt('pha','p') )
#print("phphp".count("ph",1,3))
