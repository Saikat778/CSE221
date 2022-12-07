#!/usr/bin/env python
# coding: utf-8

# In[12]:


f = open("input6.txt", mode = "r")
output_file = open("output6.txt", mode = "w")
r,c = map(int,f.readline().split())
diamond = [[0 for i in range(c)] for j in range(r)]
graph = [[0 for i in range(c)] for j in range(r)]
cd = 0
max_diamonds = 0

for i in range(r):
    line = f.readline()
    j = 0
    for j in range(c):
        graph[i][j] = line[j]
        
for i in range(r):
    for j in range(c):
        diamond[i][j] = graph[i][j]

        
def floodfill(graph, sr, sc):
    if (sr < 0 or sc < 0 or sr >= r or sc >= c) or (graph[sr][sc] == 1 or graph[sr][sc] == "#" or graph[sr][sc] == "T"):
        return 0
    
    if graph[sr][sc] == "D":
        graph[sr][sc] = "T"
        
    if graph[sr][sc] == ".":
        graph[sr][sc] = 1
    
    floodfill(graph, sr+1, sc)
    floodfill(graph, sr, sc+1)
    floodfill(graph, sr-1, sc)
    floodfill(graph, sr, sc-1)

def countingDiamonds(graph, cd):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "T":
                cd += 1
                
    return cd

for x in range(r):
    for y in range(c):
        floodfill(graph, x, y)
        diamonds = countingDiamonds(graph, cd)
        if diamonds > max_diamonds:
            max_diamonds = diamonds
        for i in range(r):
            for j in range(c):
                graph[i][j] = diamond[i][j]

print(max_diamonds, file = output_file)
output_file.close()


# In[ ]:




