#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task 2

from queue import PriorityQueue

f = open("input2.txt", mode = 'r')
output_file = open("output2.txt", mode = 'w')

def dijkstra(adj, places, start):
    visited = [False] * (places+1)
    cost = [1000] * (places+1)
    
    q = PriorityQueue()
    cost[start] = 0
    q.put((0,start))
    
    while not q.empty():
        u = q.get()
        vertex = u[1]
        if visited[vertex] == False:
            visited[vertex] = True
            for v in range(len(adj[vertex])):
                weight = adj[vertex][v][1]
                new_cost = cost[vertex] + weight
                if cost[adj[vertex][v][0]] > new_cost:
                    cost[adj[vertex][v][0]] = new_cost
                    q.put((cost[adj[vertex][v][0]], adj[vertex][v][0]))
                    
    return cost



test_cases = int(f.readline())
for i in range(test_cases):
    places,roads = map(int, f.readline().split())

    adj = [[] for m in range(places + 1)]
    for j in range(roads):
        place1, place2, weight = map(int, f.readline().split())
        adj[place1].append((place2, weight))
        adj[place2].append((place1, weight))
    cost = dijkstra(adj, places, 1)
    for i in range(len(cost)):
        if i == len(cost)-1:
            print(cost[i], file = output_file)
            
output_file.close()

