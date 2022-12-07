#!/usr/bin/env python
# coding: utf-8

# In[9]:


#task 4

from queue import Queue

input_file = open("input4.txt", mode = "r")
output_file = open("output4.txt", mode = "w")
n,m = map(int,input_file.readline().split())

adj_list = [[] for i in range (n+1)]

for i in range(m):
    u, v = map(int, input_file.readline().split())
    adj_list[u].append((v))

def cycle(source):
    vis = [0] * (n + 1)
    q = Queue()
    q.put(source)
    vis[source] = 1
    parent = 0

    while not q.empty():
        u = q.get()
        for v in range(len(adj_list[u])):
            child = adj_list[u][v]
            if vis[child] == 0:
                q.put(child)
                vis[child] = 1

            for k in range(len(adj_list[child])):
                if adj_list[child][k] == parent:
                    return "YES"
            parent = u

result = cycle(1)
if result == None:
    print("NO", file = output_file)
else:
    print(result, file = output_file)
output_file.close()


# In[ ]:




