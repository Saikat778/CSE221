#!/usr/bin/env python
# coding: utf-8

# In[7]:


#task 3

input_file = open("input2.txt", mode = "r")
output_file = open("output3.txt", mode = "w")
n,m = map(int,input_file.readline().split())

adj_list = [[] for i in range (n+1)]

for i in range(m):
    u, v = map(int, input_file.readline().split())
    adj_list[u].append((v))
    adj_list[v].append((u))

vis = [-1] * (n + 1)

def dfs(source):
    vis[source] = 1
    print(source, end =" ", file = output_file)
    for i in range(len(adj_list[source])):
        child = adj_list[source][i]
        if vis[child] == -1:
            dfs(child)

dfs(1)
output_file.close()


# In[ ]:




