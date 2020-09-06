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
        if set1 is None and set2 is None:
            return None
        #if set1 is empty, then union is full set2
        #if set2 is empty, then union is full set1
        if set1 is None or len(set1) is 0 :
            return set2;
        if set2 is None or len(set2) is 0:
            return set1;
        for outerElement in set1:
            if outerElement in union:
                continue
            union.append(outerElement)
        for outerElement in set2:
            if outerElement in union:
                continue
            union.append(outerElement)
        return union

    '''
    If an element of Set-1 is also found in Set-2,then add to intersection list
    '''
    def Intersection(set1, set2):
        intersection = []
        if set1 is None and set2 is None:
            return None
        #No need to loop through elements to find the common ones
        #if either of the sets is empty
        if set1 is None or len(set1) is 0 :
            return intersection;
        if set2 is None or len(set2) is 0:
            return intersection;
        for outerElement in set1:
            if outerElement in set2 and outerElement not in intersection:
                intersection.append(outerElement)
        return intersection

    '''
    Minus returns elements found in only one of the two sets
    '''
    def Minus(set1, set2):
        minus = []
        if set1 is None and set2 is None:
            return None
        #Empty Set-Set2 = Full Set2
        #Set1-Empty Set = Full Set1
        if set1 is None or len(set1) is 0 :
            return set2;
        if set2 is None or len(set2) is 0:
            return set1;
        if len(set1) > len(set2):
            minus.extend(set1)
            for element in set2:
                if element in minus:
                    minus.remove(element)
                else:
                    minus.append(element)
        else:
            minus.extend(set2)
            for element in set1:
                if element in minus:
                    minus.remove(element)
                else:
                    minus.append(element)
        return minus
