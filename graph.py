from graphError import GraphError
from random import randint, choice

class UndirectedGraph:
    def __init__(self, numberOfVertices, numberOfEdges):
        self.__numberOfVertices = numberOfVertices
        self.__numberOfEdges = numberOfEdges
        self.__out_neighbours = {}
        self.__edges = []
        for index in range(numberOfVertices):
            self.__out_neighbours[index] = []

    @property
    def getNumberOfVertices(self):
        return self.__numberOfVertices

    @property
    def getNumberOfEdges(self):
        return self.__numberOfEdges

    @property
    def getDictionary(self):
        return self.__out_neighbours

    @property
    def getEdges(self):
        return self.__edges

    def checkIfTheGraphHasGivenVertex(self, givenVertex):
        if givenVertex in self.__out_neighbours:
            return True
        return False

    def checkIfTheGraphHasGivenEdge(self, sourceVertex, targetVertex):
        if self.checkIfTheGraphHasGivenVertex(sourceVertex) is False:
            raise GraphError("Source vertex doesn't exist in current graph!")
        if self.checkIfTheGraphHasGivenVertex(targetVertex) is False:
            raise GraphError("Target vertex doesn't exist in current graph!")
        if int(targetVertex) == int(sourceVertex):
            raise GraphError("Target vertex is the same as source vertex!")

        if (sourceVertex, targetVertex) in self.__edges or (targetVertex, sourceVertex) in self.__edges:
            return True
        return False

    def addNewVertex(self, vertexToBeAdded):
        if self.checkIfTheGraphHasGivenVertex(vertexToBeAdded):
            raise GraphError("Vertex already exists!")
        self.__out_neighbours[vertexToBeAdded] = []
        self.__numberOfVertices += 1
        return True

    def addNewEdge(self, sourceVertex, targetVertex):
        if self.checkIfTheGraphHasGivenEdge(sourceVertex, targetVertex) is False:
            self.__out_neighbours[targetVertex].append(sourceVertex)
            self.__out_neighbours[sourceVertex].append(targetVertex)
            self.__out_neighbours[targetVertex].sort()
            self.__out_neighbours[sourceVertex].sort()
            self.__edges.append((sourceVertex, targetVertex))
            self.__numberOfEdges += 1
            return True

        return False

    def parseSetOfVertices(self):
        for vertex in self.__out_neighbours:
            yield vertex

    def parseSetOfEdgesOfAVertex(self, givenVertex):
        if self.checkIfTheGraphHasGivenVertex(givenVertex) is False:
            raise GraphError("Given vertex doesn't exist in current graph!")
        for targetVertex in self.__out_neighbours[givenVertex]:
            yield targetVertex

    def getDegreeOfGivenVertex(self, givenVertex):
        if self.checkIfTheGraphHasGivenVertex(givenVertex) is False:
            raise GraphError("Given vertex doesn't exist in current graph!")
        degree = len(self.__out_neighbours[givenVertex])
        return degree

    def removeAnEdge(self, sourceVertex, targetVertex):
        if self.checkIfTheGraphHasGivenEdge(sourceVertex, targetVertex) is False:
            raise GraphError("Provided edge doesn't exist in current graph!")
        self.__out_neighbours[targetVertex].remove(sourceVertex)
        self.__out_neighbours[sourceVertex].remove(targetVertex)
        self.__numberOfEdges -= 1


    def removeVertex(self, givenVertex):
        if self.checkIfTheGraphHasGivenVertex(givenVertex) is False:
            raise GraphError("Given vertex doesn't exist in current graph!")
        for predecessor in list(self.__out_neighbours[givenVertex]):
            self.removeAnEdge(predecessor, givenVertex)
        self.__out_neighbours.pop(givenVertex)
        self.__numberOfVertices -= 1

    def bfs(self, startVertex, visited):
        component = set()
        queue = [startVertex]
        visited[startVertex] = True

        while queue:
            vertex = queue.pop(0)
            component.add(vertex)
            for neighbour in self.__out_neighbours[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        return component

    def findConnectedComponents(self):
        visited = [False] * self.__numberOfVertices
        components = []

        for vertex in range(self.__numberOfVertices):
            if not visited[vertex]:
                component = self.bfs(vertex, visited)
                components.append(component)

        return components


def readGraphFromTextFile(textFileName):
    fileToReadFrom = open(textFileName, "rt")
    allLinesFromTextFile = fileToReadFrom.readlines()
    fileToReadFrom.close()
    newGraph = UndirectedGraph(0, 0)

    for index in range(len(allLinesFromTextFile)):
        line = allLinesFromTextFile[index].strip()
        line = line.split(' ')

        if index == 0:
            numberOfVertices = int(line[0])
            numberOfEdges = int(line[1])
            newGraph = UndirectedGraph(numberOfVertices, numberOfEdges)

        else:
            sourceVertex = int(line[0])
            targetVertex = int(line[1])
            newGraph.addNewEdge(sourceVertex, targetVertex)
    return newGraph

def writeGraphToTextFile(textFileName, graph):
    fileToWriteIn = open(textFileName, "w")
    firstLine = str(graph.getNumberOfVertices) + ' ' + str(graph.getNumberOfEdges) + '\n'
    fileToWriteIn.write(firstLine)

    for edge in graph.getEdges:
        strEdge = str(edge[0]) + ' ' + str(edge[1]) + '\n'
        fileToWriteIn.write(strEdge)
    fileToWriteIn.close()

def createRandomGraph(numberOfVertices, numberOfEdges):
    randomGraph = UndirectedGraph(numberOfVertices, 0)
    index = 0
    while index < numberOfEdges:
        try:
            added = randomGraph.addNewEdge(randint(0, numberOfVertices - 1), randint(0, numberOfVertices - 1))
        except Exception :
            added = False
        if added:
            index += 1
    return randomGraph


