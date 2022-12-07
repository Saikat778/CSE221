#!/usr/bin/env python
# coding: utf-8

# In[1]:


# task 1

input_file = open("input1.txt", mode = "r")
output_file = open("output1.txt", mode = "w")
input_data = input_file.readlines()
test_cases = int(input_data[0])

Student_id = input_data[1].strip().split(" ")
marks = input_data[2].split(" ")
length = len(Student_id)

def insert(arr1, arr2, n):
    
    for i in range(0, n - 1):
        temp = arr2[i + 1]
        temp2 = arr1[i + 1]
        j = i
        while j >= 0:
            if arr2[j] < temp:
                arr1[j + 1] = arr1[j]
            else:
                break
            j = j - 1
        arr1[j + 1] = temp2
    return arr1

result = insert(Student_id, marks, length)
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], file = output_file)
    else:
        print(result[i], end = " ", file = output_file)
    
output_file.close()

