#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task 1b

input_file = open("input1a.txt", mode = "r")
output_file = open("output1b.txt", mode = "w")
n,m = map(int,input_file.readline().split())

adj_list = [[] for i in range (n+1)]

for i in range(m):
    u, v, w = map(int, input_file.readline().split())
    adj_list[u].append((v,w))
    
for i in range(len(adj_list)):
    print("{}:".format(i), end="", file = output_file)
    for j in range(len(adj_list[i])):
        print(adj_list[i][j], end =" ", file = output_file)

    print(file = output_file)
    
output_file.close()


# In[ ]:




