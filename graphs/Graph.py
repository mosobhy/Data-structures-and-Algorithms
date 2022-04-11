'''
To review the graph data structure and its terminologies, you can
recape it from the DS notebook its good discussed there

NOTE: in this file, i am going to implement the graph data structure using 
      the adjancency list representatoin
'''

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.adjancents = {}
    
    def addAdjacent(self, vert, weight=0):
        if vert is None:
            return None
        else:
            self.adjancents[vert.id] = weight
    
    def getId(self):
        return self.id
    
    def getAdjancents(self):
        return self.adjancents.keys()

    def __str__(self):
        return f"{self.id} is connected to: { str(id for id, _ in self.adjancents.items()) }"
    

class Graph:

    def __init__(self):
        # maintain the master list of all vertices
        self.vertices = {}
        self.numVerts = 0
        self.numEdges = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        # map between the vertex's key and it whole obj
        self.vertices[key] = newVertex
        self.numVerts += 1

        return newVertex

    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.vertices:     # search for the in the vertices keys for fromvert and tovert
            newFromVertx = self.addVertex(fromVertex)
        
        if toVertex not in self.vertices:
            newToVertex = self.addVertex(toVertex)
        
        # the edge is going to be directed fromvert to tovert
        self.vertices[fromVertex].addAdjacent(self.vertices[toVertex], weight)

        # increment the edges num
        self.numEdges += 1


    def getVertex(self, key):
        try:
            vertex = self.vertices[key]
        except:
            return None
        return vertex


    def getVertices(self):
        ''' This method must return all the vertices in the graph'''
        return self.vertices.keys()


    def __contains__(self, key):
        ''' In this method we are overloading the "in" operator to search for 
        a specific key in the graph and return True if found otherwise return False '''
        return True if key in self.vertices else False

    def __iter__(self):
        ''' allow the iteration over the vertices instances in the dict (the values in dict) 
        vertices via overloading the iter operator '''
        return iter(self.vertices.values())

    
