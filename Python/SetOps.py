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
            # If this element is already present in the union, we can skip it
            # as it might have been added in union & rmeoved from set2
            # in one of the previous iteration
            if outerElement in union:
                continue
            for innerElement in set2:
                if outerElement.lower() == innerElement.lower():
                    set2.remove(innerElement) #remove the common elements
            union.append(outerElement)
        union.extend(set2) #Set2 here = (original Set2 - all common elements)
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
            # If this element is present in intersection set, It means
            # it was already compared, no need to check if it is present in Set2
            if outerElement in intersection:
                continue
            for innerElement in set2:
                if outerElement.lower() == innerElement.lower():
                    intersection.append(innerElement)
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
        for outerElement in set1:
            isFound = False
            for innerElement in set2:
                if outerElement.lower() == innerElement.lower():
                    isFound = True
                    set2.remove(innerElement) #remove the common element from set2
                    #Let the inner loop continue to remove the duplicates
            #add the element from Set1 only if it is not found in Set2 
            if not isFound:
                minus.append(outerElement)
        minus.extend(set2) #Set2 Here = (original Set2 - all common elements)
        return minus
