from graphError import GraphError
from random import randint, choice

class UndirectedGraph:
    def __init__(self, numberOfVertices, numberOfEdges):
        self.__numberOfVertices = numberOfVertices
        self.__numberOfEdges = numberOfEdges
        self.__dictionary = {}
        for index in range(numberOfVertices):
            self.__dictionary[index] = []

    @property
    def getNumberOfVertices(self):
        return self.__numberOfVertices

    @property
    def getNumberOfEdges(self):
        return self.__numberOfEdges

    @property
    def getDictionary(self):
        return self.__dictionary

    def checkIfTheGraphHasGivenVertex(self, givenVertex):
        if givenVertex in self.__dictionary:
            return True
        return False

    def checkIfTheGraphHasGivenEdge(self, sourceVertex, targetVertex):
        if self.checkIfTheGraphHasGivenVertex(sourceVertex) is False:
            raise GraphError("Source vertex doesn't exist in current graph!")
        if self.checkIfTheGraphHasGivenVertex(targetVertex) is False:
            raise GraphError("Target vertex doesn't exist in current graph!")

        if sourceVertex not in self.__dictionary[targetVertex] and targetVertex not in self.__dictionary[sourceVertex]:
            return False
        return True

    def addNewVertex(self, vertexToBeAdded):
        if self.checkIfTheGraphHasGivenVertex(vertexToBeAdded):
            raise GraphError("Vertex already exists!")
        self.__dictionary[vertexToBeAdded] = []
        self.__numberOfVertices += 1
        return True

    def addNewEdge(self, sourceVertex, targetVertex):
        if self.checkIfTheGraphHasGivenVertex(sourceVertex) is False:
            raise GraphError("Source vertex doesn't exist in current graph!")
        if self.checkIfTheGraphHasGivenVertex(targetVertex) is False:
            raise GraphError("Target vertex doesn't exist in current graph!")

        if sourceVertex in self.__dictionary[targetVertex] or targetVertex in self.__dictionary[sourceVertex]:
            raise GraphError("The edge already exists!")
        self.__dictionary[targetVertex].append(sourceVertex)
        self.__dictionary[sourceVertex].append(targetVertex)
        self.__numberOfEdges += 1
        return True

    def parseSetOfVertices(self):
        for vertex in self.__dictionary:
            yield vertex

    def parseSetOfEdgesOfAVertex(self, givenVertex):
        if self.checkIfTheGraphHasGivenVertex(givenVertex) is False:
            raise GraphError("Given vertex doesn't exist in current graph!")
        for targetVertex in self.__dictionary[givenVertex]:
            yield targetVertex

    def getDegreeOfGivenVertex(self, givenVertex):
        if self.checkIfTheGraphHasGivenVertex(givenVertex) is False:
            raise GraphError("Given vertex doesn't exist in current graph!")
        degree = len(self.__dictionary[givenVertex])
        return degree

    def removeAnEdge(self, sourceVertex, targetVertex):
        if self.checkIfTheGraphHasGivenEdge(sourceVertex, targetVertex) is False:
            raise GraphError("Provided edge doesn't exist in current graph!")
        self.__dictionary[targetVertex].remove(sourceVertex)
        self.__dictionary[sourceVertex].remove(targetVertex)
        self.__numberOfEdges -= 1


    def removeVertex(self, givenVertex):
        if self.checkIfTheGraphHasGivenVertex(givenVertex) is False:
            raise GraphError("Given vertex doesn't exist in current graph!")
        for predecessor in list(self.__dictionary[givenVertex]):
            self.removeAnEdge(predecessor, givenVertex)
        self.__dictionary.pop(givenVertex)
        self.__numberOfVertices -= 1


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
            newGraph.getDictionary[targetVertex].append(sourceVertex)
            newGraph.getDictionary[sourceVertex].append(targetVertex)
    return newGraph

def writeGraphToTextFile(textFileName, graph):
    fileToWriteIn = open(textFileName, "w")
    firstLine = str(graph.getNumberOfVertices) + ' ' + str(graph.getNumberOfEdges) + '\n'
    fileToWriteIn.write(firstLine)

    for vertex in graph.getDictionary.keys():
        if graph.getDegreeOfGivenVertex(vertex) == 0:
            nextLine = str(vertex) + '\n'
            fileToWriteIn.write(nextLine)
        else:
            for outVertex in graph.getDictionary[vertex]:
                if vertex < outVertex:
                    nextLine = str(vertex) + ' ' + str(outVertex) + '\n'
                    fileToWriteIn.write(nextLine)

    fileToWriteIn.close()

def createRandomGraph(numberOfVertices, numberOfEdges):
    randomGraph = UndirectedGraph(numberOfVertices, 0)
    # allPossibilitiesForSourceVertex = list(range(numberOfVertices))
    #
    # while numberOfEdges > 0:
    #     sourceVertex = choice(allPossibilitiesForSourceVertex)
    #     allPossibilitiesForSourceVertex.remove(sourceVertex)
    #     allPossibilitiesForTargetVertex = list(range(numberOfVertices))
    #
    #     while len(allPossibilitiesForTargetVertex) > 0 and numberOfEdges > 0:
    #         targetVertex = choice(allPossibilitiesForTargetVertex)
    #         allPossibilitiesForTargetVertex.remove(targetVertex)
    #         randomGraph.addNewEdge(sourceVertex, targetVertex)
    #         numberOfEdges -= 1

    index = 0
    while index < numberOfEdges:
        if randomGraph.addNewEdge(randint(0, numberOfVertices - 1), randint(0, numberOfVertices - 1)):
            index += 1

    return randomGraph
