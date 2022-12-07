#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task 1

# we cannot use BFS because there are weights assigned to the path. BFS gives the shortest path based on the minimum number 
# of nodes we need to travel to reach the goal, assuming that all path have the equal distance or weight. But Dijkstra gives
# the shortest path based on the weights it needs to travel to reach the goal.

from queue import PriorityQueue

f = open("input1.txt", mode = "r")
t_output = open("output1a.txt", mode = "w")

vertices, edges = map(int, f.readline().split())
list1 = []
adj = [[] for i in range(vertices)] 

#converting letters into numbers
for i in range(edges):
    n,m,w = map(str, f.readline().split())
    if n not in list1:
        list1.append(n)
    if m not in list1:
        list1.append(m)
    print(list1.index(n), list1.index(m), w, file = t_output)

t_output.close()
f2 = open("output1a.txt", mode = "r")
m_output = open("output1.txt", mode = "w")

for i in range(edges):
    n,m,w = map(int, f2.readline().split())
    adj[n].append((m,w))
    adj[m].append((n,w))

#dijkstra algorithm    
    
def dijkstra(start):
    visited = [False] * vertices
    cost = [1000] * vertices
    parent = [-1] * vertices
    
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
                    parent[adj[vertex][v][0]] = vertex
                    q.put((cost[adj[vertex][v][0]], adj[vertex][v][0]))
    return cost, parent

cost, parent = dijkstra(0)
cost_dict = {}
dict2 = {}
con_parent = [-1]*len(list1)
for i in range(1, len(list1)):
    con_parent[i] = list1[parent[i]]

for i in range(len(list1)):
    cost_dict[list1[i]] = cost[i]
    dict2[list1[i]] = con_parent[i]
shortest_path2 = []

# shortest_path

def short_path(dest):
    u = dest
    if dict2[u] == -1:
        return
    shortest_path2.append(dict2[u])
    u = dict2[u]
    short_path(u)
    
def cost_dest(dest):
    print("", file = m_output)
    print("Cost:",cost_dict[dest], file = m_output)
    
short_path('MOGHBAZAR')
length = len(shortest_path2)
shortest_path = [0] * length
for i in range(len(shortest_path2)):
    shortest_path[i] = shortest_path2[length-1-i]
print("Shortest path:", end = " ", file = m_output)
for i in range(len(shortest_path)):
    print(shortest_path[i], end =" ", file = m_output)
cost_dest('MOGHBAZAR')

m_output.close()

