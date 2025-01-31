import math
import numpy as np
import time

'''
Design

Divide:
    - split the array into thirds and remember the index of these points

Conquer
    - solve new smaller array
    - base case when array is of size 1

Merge:
    - Compare the elements in each array and store the new value in the correct order sorting the array

split the array
- if of size < 3 sort elements and return
'''

def tryMerge(array):
    print(array)
    tryMergeHelper(array,0,len(array)-1)
    print(array)
    return 

def tryMergeHelper(array,start,end):

    if(end - start == 0):
        return 
    elif(end - start == 1):
        sort(array,start,end)
        return 
    else:
        first = math.ceil(start+(end-start)/3)
        second = math.floor(start+2*(end-start)/3)

        tryMergeHelper(array,start,first-1)
        tryMergeHelper(array,first,second)
        tryMergeHelper(array,second+1,end)

        merge(array,start,first,second,end)
    return 

def merge(array,left,mid1,mid2,right):

    n1 = mid1 - left
    n2 = mid2 - mid1 + 1
    n3 = right - mid2

    L = [0] * n1
    M = [0] * n2
    R = [0] * n3

    for i in range(n1):
        L[i] = array[left + i]
    for j in range(n2):
        M[j] = array[mid1 + j]
    for k in range(n3):
        R[k] = array[mid2 + k + 1]

    i = 0
    j = 0
    k = 0
    l = left

    while i < n1 and j < n2 and k < n3:
        if(L[i] <= M[j] and L[i] <= R[k]):
            array[l] = L[i]
            i+=1
        elif(M[j] <= R[k]):
            array[l] = M[j]
            j+=1
        else:
            array[l] = R[k]
            k+=1
        l += 1


    while i < n1 and j < n2:
        if L[i] <= M[j]:
            array[l] = L[i]
            i+=1
        else:
            array[l] = M[j]
            j+=1
        l+=1

    while i < n1 and k < n3:
        if L[i] <= R[k]:
            array[l] = L[i]
            i+=1
        else:
            array[l] = R[k]
            k+=1
        l+=1

    while j < n2 and k < n3:
        if M[j] <= R[k]:
            array[l] = M[j]
            j+=1
        else:
            array[l] = R[k]
            k+=1
        l+=1

    while i < n1:
        array[l] = L[i]
        i+=1
        l+=1 
    while j < n2:
        array[l] = M[j]
        j+=1
        l+=1 
    while k < n3:
        array[l] = R[k]
        k+=1
        l+=1 

    return
    
def sort(array,start,end):
    if(array[end] < array[start]):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp

    return



test_array = np.array([4,6,5,3,8,4,12312,514])
start = time.time()
tryMerge(test_array)
elapsed = time.time() - start

print(elapsed)
