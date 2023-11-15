from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    z = 0
    
    while len(frontier) != 0:
        
        w = result
        for x in frontier:
            result.update(graph[x])
            frontier.update(graph[x])
            
            q = x
            break
        frontier.remove(q)
        if w == result and z > 10:
            break
        z += 1
        
    
    return result

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    print(reachable(graph, 'A'))




def connected(graph):
    reachable(graph, next(iter(graph)))
    return len(graph) == len(reachable(graph, next(iter(graph))))




def n_components(graph):
    cycles = set()
    for i in graph:
        x = reachable(graph, next(iter(i)))
        print(x)
        cycles.add(len(x))
    print(cycles)

    if len(graph) in cycles:
        return 1
    else:
        return len(cycles)
