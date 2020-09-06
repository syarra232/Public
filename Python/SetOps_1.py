#!/usr/bin/python

import os
import sys

class SetOps:

    def __init__(self):
        return
    '''
    Remove the common elements from Set2 to avoid duplication
    Then add elements of both Set-1 & Set-2 to union set
    '''
    def Union(set1, set2):
        union = []
        if set1 is None or set2 is None:
            return None
        for outerElement in set1:
            for innerElement in set2:
                if outerElement.lower() == innerElement.lower():
                    set2.remove(innerElement)
        union.extend(set1)
        union.extend(set2)
        return union
    '''
    If an element of Set-1 is also found in Set-2,then add to intersection list
    '''
    def Intersection(set1, set2):
        intersection = []
        if set1 is None or set2 is None:
            return None
        for outerElement in set1:
            for innerElement in set2:
                if outerElement.lower() == innerElement.lower():
                    intersection.append(innerElement)
        return intersection
    '''
    Remove the commmon elements from both Set-1 & Set-2 first
    Then add both the sets to minus set
    '''
    def Minus(set1, set2):
        minus = []
        if set1 is None or set2 is None:
            return None
        for outerElement in set1:
            isFound = False
            for innerElement in set2:
                if outerElement.lower() == innerElement.lower():
                    #set1.remove(outerElement)
                    isFound = True
                    set2.remove(innerElement)
                    #Let the inner loop continue to remove the duplicates
            if not isFound:
                minus.append(outerElement)
        #minus.extend(set1)
        minus.extend(set2)
        return minus
