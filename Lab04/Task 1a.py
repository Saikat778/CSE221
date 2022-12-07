#!/usr/bin/env python
# coding: utf-8

# In[9]:


#task 1a

f = open("input1a.txt", mode = "r")
output_file = open("output1a.txt", mode = "w")
vertix, edges = map(int,f.readline().split())
listGraph = [[0 for i in range(vertix+1)] for j in range(vertix+1)]

def buildGraphUsingListofLists(src, des, weight):
    listGraph[src][des] = weight
    return listGraph

for i in range(1,edges+1):
    src, des, weight = map(int, f.readline().split())
    result = buildGraphUsingListofLists(src, des, weight)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end =" ", file = output_file)
    print("", file = output_file)
    
output_file.close()


# In[7]:





# In[ ]:




