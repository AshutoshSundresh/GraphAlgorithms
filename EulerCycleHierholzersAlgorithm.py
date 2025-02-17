from collections import defaultdict

def find_eulerian_cycle(graph):
    adj_list = {node: edges[:] for node, edges in graph.items()} 
    stack = ['a']  # start from any vertex, here 'a'
    circuit = []

    while stack:
        v = stack[-1]
        if adj_list[v]:  # if the vertex has remaining edges
            next_v = adj_list[v].pop()
            adj_list[next_v].remove(v)  # remove the edge both ways
            stack.append(next_v)
        else:
            circuit.append(stack.pop())  # backtrack when no edges left

    return circuit[::-1]  # reverse to get the correct order

# question 32, section 8.1
graph = {
    'a': ['b', 'h'],
    'b': ['a', 'c', 'd', 'f'], 
    'c': ['b', 'h', 'd', 'i'],
    'd': ['b', 'c', 'e', 'i'], 
    'e': ['d', 'i', 'f', 'j'],
    'f': ['b', 'e', 'g', 'j'], 
    'g': ['f', 'j'],
    'h': ['a', 'c', 'i', 'j'], 
    'i': ['c', 'e', 'h', 'd'], 
    'j': ['e', 'f', 'g', 'h'] 
}

eulerian_cycle = find_eulerian_cycle(graph)
print("Eulerian Cycle:", ",".join(eulerian_cycle))
