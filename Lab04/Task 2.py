#!/usr/bin/env python
# coding: utf-8

# In[3]:


#task 2

from queue import Queue

input_file = open("input2.txt", mode = "r")
output_file = open("output2.txt", mode = "w")
n,m = map(int,input_file.readline().split())

adj_list = [[] for i in range (n+1)]

for i in range(m):
    u, v = map(int, input_file.readline().split())
    adj_list[u].append((v))
    adj_list[v].append((u))


def bfs(source):
    vis = [0] * (n + 1)

    q = Queue()
    q.put(source)
    vis[source] = 1

    while not q.empty():
        u = q.get()
        print(u, end =" ", file = output_file)

        for v in range(len(adj_list[u])):
            child = adj_list[u][v]
            if vis[child] == 0:
                q.put(child)
                vis[child] = 1

bfs(1)
output_file.close()


# In[ ]:




