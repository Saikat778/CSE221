#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# task 4i

queue = []
value_list = []
queue_div = []
split = []

input_file = open("input5.txt", mode = "r")
output_file = open("output5a.txt", mode = "w")
input_data = input_file.readlines()

for i in range(len(input_data)):
    value = input_data[i].strip().split("/n")
    val_str = ""
    for x in value:
        val_str += ""+ x
    value_list.append(val_str)

    
def enqueue(name):
    split = name.split(" ")
    queue.append(split[0])
    queue_div.append(split[1])

    for i in range(len(queue_div)):
        for j in range(0, len(queue_div) - i - 1):
            if queue_div[j] > queue_div[j + 1]:
                temp = queue_div[j]
                queue_div[j] = queue_div[j+1]
                queue_div[j+1] = temp
                temp2 = queue[j]
                queue[j] = queue[j+1]
                queue[j+1] = temp2


def seeDoctor(queue, queue_div):
    temp = queue[0]
    queue.remove(queue[0])
    queue_div.remove(queue_div[0])
    printQueue(temp)
    
def printQueue(temp):
    print(temp, file = output_file)
    
for i in range(len(value_list)):
    if value_list[i] != "see doctor":
        enqueue(value_list[i])
    else:
        seeDoctor(queue, queue_div)
        
output_file.close()

# task 4ii

# task 4

queue = []
value_list = []
queue_div = []
split = []

input_file = open("input5.txt", mode = "r")
output_file = open("output5b.txt", mode = "w")
input_data = input_file.readlines()

for i in range(len(input_data)):
    value = input_data[i].strip().split("/n")
    val_str = ""
    for x in value:
        val_str += ""+ x
    value_list.append(val_str)

def heapify(queue, queue_div, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and queue_div[i] > queue_div[l]:
        largest = l
    if r < n and queue_div[largest] > queue_div[r]:
        largest = r
    if largest != i:
        queue_div[i], queue_div[largest] = queue_div[largest], queue_div[i]
        queue[i], queue[largest] = queue[largest], queue[i]
        heapify(queue, queue_div, n, largest)

def insert(name):
    split = name.split(" ")
    queue.append(split[0])
    queue_div.append(split[1])
    size = len(queue_div)
    for i in range((size//2)-1, -1, -1):
        heapify(queue, queue_div, size, i)
        
def sink(queue, queue_div):
    temp = queue[0]
    queue_div.remove(queue_div[0])
    queue.remove(queue[0])
    size = len(queue)
    printQueue(temp)
    for i in range((size//2)-1, -1, -1):
        heapify(queue, queue_div, size, i)

def printQueue(temp):
    print(temp, file = output_file)
        
for i in range(len(value_list)):
    if value_list[i] != "see doctor":
        insert(value_list[i])
    else:
        sink(queue, queue_div)
        
output_file.close()

# task 4iii

import time 
import math 
import matplotlib.pyplot as plt 
import numpy as np 
#change the value of n for your own experimentation 

n = 30 
x = [i for i in range(n)] 
y = [0 for i in range(n)] 
z = [0 for i in range(n)] 

for i in range(n-1):
    start = time.time() 
    enqueue(x[i+1]) 
    y[i+1]= time.time()-start 
    start = time.time() 
    heapify(x[i+1]) 
    z[i+1]= time.time()-start 
    
x_interval = math.ceil(n/10) 
plt.plot(x, y, 'r') 
plt.plot(x, z, 'b') 
plt.xticks(np.arange(min(x), max(x)+1, x_interval)) 
plt.xlabel('n-th position') 
plt.ylabel('time') 
plt.title('Comparing Time Complexity!') 
plt.show() 

