#!/usr/bin/env python
# coding: utf-8

# In[6]:


# task 3i

input_file = open("input2.txt", mode = "r")
output_file = open("output3a.txt", mode = "w")
input_data = input_file.readlines()

test_cases = int(input_data[0])
number = input_data[1].split(" ")
num = []

for i in range(test_cases):
    num.append(int(number[i]))

def partition(array, low, high):
    
    pivot = array[high]
    i = low - 1 
    for j in range (low, high):
        if array[j] < pivot:
            i=i+1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1) 
        quickSort(array, pi + 1, high)
        
    return array

result = quickSort(num, 0, len(num) -1)
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], file = output_file)
    else:
        print(result[i], end = " ", file = output_file)
    
output_file.close()

# task 3ii

input_file = open("input3.txt", mode = "r")
output_file = open("output3b.txt", mode = "w")
input_data = input_file.readlines()

number = input_data[0].split(" ")
num = []
key_str = []

for i in range(2,len(number)):
    num.append(int(number[i]))
    
for i in range(1,len(input_data)):
    key_str.append(input_data[i].strip().split(" "))


def partition(num, key, low, high):
    
    pivot = num[high]
    i = low - 1
    for j in range (low, high+1):
        if num[j] <= pivot:
            i=i+1
        if i == int(key) - 1:
            return num[j]

def findk(num, key):
    temp_result = []
    for i in range(len(key)):
        temp_result.append(partition(num, key[i][1], 0, len(num) - 1))
    
    return temp_result


result = findk(num, key_str)
for i in range(len(result)):
    print(result[i], file = output_file)

output_file.close()

