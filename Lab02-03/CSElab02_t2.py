#!/usr/bin/env python
# coding: utf-8

# In[2]:


# task 2

input_file = open("input2.txt", mode = "r")
output_file = open("output2.txt", mode = "w")
input_data = input_file.readlines()

test_cases = int(input_data[0])
number = input_data[1].split(" ")
num = []
for i in range(test_cases):
    num.append(int(number[i]))

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l  
 
    while i < len(L) and j < len(R):
        
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr

result = mergeSort(num, 0, test_cases-1)

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], file = output_file)
    else:
        print(result[i], end = " ", file = output_file)
    
output_file.close()

