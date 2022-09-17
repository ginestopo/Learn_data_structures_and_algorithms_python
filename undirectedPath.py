"""
                    UNDIRECTED PATH  

Tutorial https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1050s&ab_channel=freeCodeCamp.org

Author: Gines Diaz

Complexity         Time: O(e) Space: O(n)  where e are edges and n are nodes     

            i--------j
            |      /  
            |    /      
            |  /       
            k--------l
            |
            |
            |
            m

            o--------n

We convert from edges to path:
Conversion from edges to path. In edges, "i" is connected to "j" --> "i":["j"..] but also "j" is connected to "i" "j":["i"]

A common thing is that our undirected graph has a cicle (in this case i,j,k). Let's handle this.

"""


from tkinter import CURRENT


edges =[
    ["i","j"],
    ["k","i"],
    ["k","j"],
    ["m","k"],
    ["k","l"],
    ["o","n"]
]

edges1 = [
    ["a","b"],
    ["a","c"],
    ["b","c"],
    ["c","d"],
    ["b","d"],
    ["d","f"]
]

''' EXAMPLE AFTER CONVERSION edges --> path
path = {
    "i":["j","k"],
    "j":["i","k"],
    "k":["i","j","m","l"],
    "m":["k"],
    "l":["k"],
    "o":["n"],
    "n":["o"]
}
'''

#Auxiliary function to convert from edges to graph
def buildGraph(edges):
    graph = {}

    for edge in edges:
        a,b = edge
        if(a not in graph): graph[a] = []
        if(b not in graph): graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph


#we can implement either DepthFirst or [BreathFirst] to find if a path exists between nodeA and nodeB
def undirectedPath(edges, nodeA, nodeB):
    graph=buildGraph(edges)
    return hasPath(graph, nodeA, nodeB)
    

#BreathFirst implementation but a bit modified to ignored visited nodes
#This way we avoid loops
def hasPath(graph, nodeA, nodeB):
    queue = []
    queue.append(nodeA)

    visited = []

    while(queue):
        current = queue.pop(0)
        visited.append(current)

        if(current == nodeB):
            return True

        for x in graph[current]:
            if(x not in visited):
                queue.append(x)

    return False


print(undirectedPath(edges1, "a","f"))