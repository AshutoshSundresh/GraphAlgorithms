# backtracking algorithm

def is_valid(v, pos, path, graph):
    if v not in graph[path[pos - 1]]: 
        return False
    if v in path:  
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph): 
        return path[0] in graph[path[pos - 1]]  

    for v in graph:
        if is_valid(v, pos, path, graph):
            path[pos] = v 
            if hamiltonian_cycle_util(graph, path, pos + 1): 
                return True
            path[pos] = -1  

    return False

def find_hamiltonian_cycle(graph):
    path = [-1] * len(graph)  
    start = list(graph.keys())[0]  
    path[0] = start

    if not hamiltonian_cycle_util(graph, path, 1):
        print("Exiting")
        return None
    
    path.append(path[0]) 
    return path

# section 8.3 question 1
graph = {
    'd': ['a', 'i'],
    'a': ['d', 'e', 'i', 'b'],
    'i': ['d', 'a', 'e', 'f'],
    'e': ['a', 'i', 'f', 'b'],
    'b': ['a', 'e', 'g', 'c'],
    'c': ['b', 'g', 'h'],
    'h': ['c', 'g', 'j'],
    'j': ['f', 'h'],
    'f': ['j', 'g', 'e', 'i'],
    'g': ['b', 'c', 'f', 'h']
}

hamiltonian_cycle = find_hamiltonian_cycle(graph)
if hamiltonian_cycle:
    print("Hamiltonian Cycle:", ",".join(hamiltonian_cycle))
