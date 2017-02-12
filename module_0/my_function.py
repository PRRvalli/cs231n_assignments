#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 05:04:47 2017

@author: prr


"""
def quicksort(arr):
    if(len(arr)<=1):
        return arr
    pivot=arr[len(arr)/2]
    left=[x for x in arr if x < pivot]
    right=[x for x in arr if x > pivot]
    middle=[x for x in arr if x == pivot]
    print left+middle+right
    return quicksort(left)+middle+quicksort(right)


def even_cubes(arr):
    return {x:x**3 for x in arr if x%2==0}

