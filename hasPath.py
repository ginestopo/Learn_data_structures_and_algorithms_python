def hasPathDepth(graph,src,dst):
    if src == dst:
        return True
   
    for x in graph[src]:
        if(hasPathDepth(graph,x,dst)==True):
            return True
    
    return False



def hasPathBreath(graph,src,dst):
    if src == dst:
        return True
    
    queue = [src]

    while(queue):
        current = queue.pop(0)
        
        if(current == dst):
            return True
        
        for x in graph[current]:
            queue.append(x)

    return False



graph = {
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}

graph2 = {
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}


print(hasPathDepth(graph,"a","f"))
print(hasPathBreath(graph,"a","f"))

print(hasPathDepth(graph2,"a","x"))
print(hasPathBreath(graph2,"a","x"))