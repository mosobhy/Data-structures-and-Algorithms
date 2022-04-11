'''
here in this file i am going to test the graph implementation in
the graph.py file
'''

from Graph import Graph

def main():
    
    # create a graph instance
    graph = Graph()

    # add random vertices
    for i in range(6):
        graph.addVertex(i)

    # add edges between the vertcies
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 5, 2)

    graph.addEdge(1, 2, 4)

    graph.addEdge(2, 3, 9)

    graph.addEdge(3, 4, 7)
    graph.addEdge(3, 5, 3)

    graph.addEdge(4, 0, 1)

    graph.addEdge(5, 2, 1)
    graph.addEdge(5, 4, 8)

    # print out the graph
    for node in graph:
        # get the edges between nodes and its weight
        for id, weight in node.adjancents.items():
            print(f'({node.id}, {id} wiht weight: {weight})')


# main call
if __name__ == '__main__':
    main()