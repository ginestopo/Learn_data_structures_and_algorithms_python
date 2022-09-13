"""
                    Breath First QUEUE O(V+E) 

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

1º      Print: A     Queue: B,C
2º      Print: C     Queue: E,B                     "FIFO in the queue (first was C, so C out first)"
3º      Print: B     Queue: D,E
4º      Print: E     Queue: D
5º      Print: D     Queue: F
6º      Print: F     Queue: 


Note: Breath First and Depth First are ALMOST IDENTICAL, only pop() or pop(0) is used in depth and breath respectively
"""

from multiprocessing import current_process


def breathFirst(graph,source):
    queue = [source]

    while(queue):
        current = queue.pop(0)
        print(current)

        for x in graph[current]:
            queue.append(x)
    

graph = {
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}

breathFirst(graph,"a")