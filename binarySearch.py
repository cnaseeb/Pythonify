#!/usr/bin/python

#Binary search
def binarySearch(list, value):
    first = 0
    last = len(list)-1
    result = False
    
    while first <= last and not result:
        midpoint = (first + last)//2
        if(midpoint == value):
            result = True
            
        else:
            if value < list[midpoint]:
                last = midpoint -1
            else:
                first = midpoint + 1
                
    return result          
    


listToSearchIn = [1, 5, 7, 12, 14, 63, 70, 72, 81, 87, 98, 102]

bSearch1 = binarySearch(listToSearchIn, 3)
bSearch1

bSearch2 = binarySearch(listToSearchIn, 5)
bSearch2
