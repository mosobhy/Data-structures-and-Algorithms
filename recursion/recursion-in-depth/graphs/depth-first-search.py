# NOTE: also look at the implmentation of CS50 AI course implementation using
# the stack data structure, its very cool one and also for the BFS
# this function is based on the implementation of the Graph.py file

def depthFirstSearch(graph, visited=[], goal):

    if graph == None:
        return False
    if graph.data = goal:
        return True

    # get and traverse the neighbours of a node
    for node in graph.getNeighbours():
        if node not in visited:
            visited.append(node)
            # recusively traverse every neighbour of the node
            return depthFirstSearch(node, visited, goal)

    return False
