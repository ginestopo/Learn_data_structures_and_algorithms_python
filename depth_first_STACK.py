"""
                    Depth First STACK O(V+E) 

Tutorial https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1050s&ab_channel=freeCodeCamp.org

Author: Gines Diaz

Complexity          O(V+E)      where V are vertices and E are edges

            A------->C
            |        |
            |        |
            v        v
            B        E
            |
            |
            v
            D------->F

1º      Print: A     Stack(top of stack is right): C,B
2º      Print: B     Stack: C,D                     "we pop B from the stack in step one, and continue the path in B"
3º      Print: D     Stack: C,F
4º      Print: F     Stack: C
5º      Print: C     Stack: E
6º      Print: E     Stack: 
"""

from queue import Empty

#Explicit algorithm
def depthFirstGraph(graph,source):
    stack = [source]

    while(stack):
        current = stack.pop()
        print(current)

        for x in graph[current]:
            stack.append(x)

#This is a short alternative using recursion
def depthFirstGraphRecursive(graph,source):
    print(source)

    for x in graph[source]:
        depthFirstGraphRecursive(graph,x)

graph = {
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}

depthFirstGraph(graph,"a")
print()
depthFirstGraphRecursive(graph,"a")
