#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task 5
from queue import PriorityQueue

f = open("input5.txt", mode = 'r')
o = open("output5.txt", mode = 'w')
test_cases = int(f.readline())

def dijkstra(start):
    visited = [False] * (places+1)
    cost = [1000] * (places+1)
    
    q = PriorityQueue()
    
    cost[start] = 0
    q.put((0,start*-1))
    while not q.empty():
        u = q.get()
        vertex = u[1]*-1
        if visited[vertex] == False:
            visited[vertex] = True
            for v in range(len(adj[vertex])):
                weight = adj[vertex][v][1]
                if cost[vertex] != 0:
                    mini = min(cost[vertex], weight)
                    cost[adj[vertex][v][0]] = mini
                else:
                    cost[adj[vertex][v][0]] = weight

                q.put((cost[adj[vertex][v][0]]*-1, adj[vertex][v][0]*-1))
                    
    return cost
def printCost(cost):
    for i in (cost[1:]):
        if i == 1000:
            print(-1, end =" ", file = o)
        else:
            print(i, end = " ", file = o)
    print(" ", file = o)

for i in range(test_cases):
    places,roads = map(int, f.readline().split())

    adj = [[] for m in range(places + 1)]
    for j in range(roads):
        place1, place2, weight = map(int, f.readline().split())
        adj[place1].append((place2, weight))
    source = int(f.readline())
    cost = dijkstra(source)
    printCost(cost)
    
o.close()

