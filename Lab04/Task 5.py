#!/usr/bin/env python
# coding: utf-8

# In[11]:


f = open("input5.txt", mode = "r")
output_file = open("output5.txt", mode = "w")
c,r,d = map(int,f.readline().split())

def buildGraphUsingDictionary(r,f):
    graph = {}
    counter = 0
    while (counter<r):
        line = f.readline()
        a,b = line.split(" ")
        b = b.strip() 
        a=int(a)
        b=int(b)
        if(a in graph):
            graph[a].append(b)
        if(b in graph):
            graph[b].append(a)
        if(a not in graph):
            graph[a]=[b]
        if(b not in graph):
            graph[b]=[a]
        counter+=1
    return graph

def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        print("Same Node", file = output_file)
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path
            explored.append(node)
 
    print("Doesn't exist", file = output_file)
    return

result = buildGraphUsingDictionary(r,f)
path = BFS_SP(result, 1, d)
time = 0
for i in range(1, len(path)):
    time += 1
    
print("Times:",time, file = output_file)
print("Shortest path:", end = " ", file = output_file)
for i in range(0, len(path)):
    print(path[i], end = " ", file = output_file)
    
output_file.close()


# In[ ]:




