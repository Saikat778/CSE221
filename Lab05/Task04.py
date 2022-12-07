#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task 4i

# If there are N places and M roads, the time complexities of the solutions provided in problem 1 & problem 2 are O(MlogN).
# It takes O(|V|) time to construct the initial priority queue of |V| vertices. Then iterating over all vertices’ neighbors
# and updating their cost values over the course of a run of the algorithm takes O(|E|) time.  for each iteration of the 
# loop time taken is O(|V|) as one vertex is removed from Q per loop.Then to extract-min distance nodes and update an 
# element it takes O(log|V|) time.

# The total time is O(M*logN)

#task 4ii

# If the number of titans in each road is exactly 1, we can use BFS to solve this problem.
# For the input file we need to add the destination node and we can remove the wieght of the path since it's 1 for all
# the paths. 

f = open("input4.txt", mode = "r")
output_file = open("output4.txt", mode = "w")
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

