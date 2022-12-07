#!/usr/bin/env python
# coding: utf-8

# In[3]:


# CSE221 Lab 03 Graphs
def readFile():
# reading file from as input
# change the file name according to yours
    f = open("graph.txt", "r")

# first line of input contains the number of vertices in the graph
    n = f.readline()
 # strip() gets rid of the new line
 # try printing n without strip()
    print(n.strip())
    n = n.strip()
    print(type(n))
    # n is of type string. we need to convert it to int
    n=int(n)
    print(type(n))

     # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    print(c)
    buildGraphUsingDictionary(5,f)
    buildGraphUsingListofLists(5,f)
# we want to build an adjacency list like the following
# A -> B,C
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}
def buildGraphUsingDictionary(c,f):
    graph = {}
    counter = 0
    while (counter<=c):
        line = f.readline() # reading each line
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        a=int(a)
        b=int(b)
   
        if(a in graph):
            graph[a].append(b)
        else:
            graph[a]=[b]
  #  print(a)
  #  print(b)
        counter+=1
        print(graph)

    printGraph(graph, None)


# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
 # 1 -> 2,4
 # 2 -> 4
 # 3 -> 1,4
 # 4 -> 2
# notice this method takes both the graphs as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph
def printGraph(graph,listGraph):
    if listGraph == None:
        for i in range(1, len(graph) + 1):
            print(i, end = " -> ")
            for j in range(len(graph[i])):
                if j == len(graph[i]) - 1:
                    print(graph[i][j])
                else:
                    print(graph[i][j], end = ",")
                    

    if graph == None:
        nonZero = 0
        count = 1
        for i in range(1,len(listGraph)):
            print(i, end = " -> ")
            for k in range(len(listGraph[i])):
                if listGraph[i][k] != 0:
                    nonZero +=1
            for j in range(len(listGraph[i])):
                if listGraph[i][j] != 0:
                    if count == nonZero:
                        print(j)
                    else:
                        print(j, end =",")
                        count+=1
            nonZero = 0
            count = 1
        
 # Your code
# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c,f):
    listGraph = [] # do not change the name of the variable
    for i in range(c):
        listGraph = [[0 for i in range(c)] for j in range(c)]
    
    counter = 0
    while (counter<=c):
        line = f.readline() # reading each line
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        a=int(a)
        b=int(b)
        listGraph[a][b] = 1
   
        counter+=1
 # your code
    print(listGraph)
    printGraph(None,listGraph)
# ======================Program starts here.========================
# read file using the readFile() method readFile()
readFile()


# In[ ]:




