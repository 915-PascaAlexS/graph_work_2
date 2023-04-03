from graph import UndirectedGraph, readGraphFromTextFile, writeGraphToTextFile, createRandomGraph
from graphError import GraphError
from copy import deepcopy

class Ui:
    def __init__(self):
        self.__allCommands = {
            '1': self.addVertex,
            '2': self.removeVertex,
            '3': self.addEdge,
            '4': self.removeEdge,
            '5': self.getNumberOfVertices,
            '6': self.getNumberOfEdges,
            '7': self.parseTheSetOfVertices,
            '8': self.verifyIfThereIsAnEdgeBetweenTwoVertices,
            '9': self.getDegreeOfAVertex,
            '10': self.parseSetOfEdgesOfAVertex,
            '11': self.createRandomGraph,
            '12': self.createACopyOfTheGraph,
            '13': self.readGraphFromTextFile,
            '14': self.writeGraphToTextFile,
            '15': self.switchCurrentGraph,
            '16': self.findConnectedComponentsOfGraph
        }
        self.__listOfGraphs = []
        self.__indexOfCurrentGraph = None


    def createRandomGraph(self):
        numberOfVertices = int(input("Enter the number of vertices: "))
        numberOfEdges = int(input("Enter the number of edges: "))
        if numberOfEdges > numberOfVertices ** 2:
            raise GraphError("Too many edges!")
        if numberOfEdges < 0 or numberOfEdges < 0:
            raise GraphError("Invalid input!")
        self.__listOfGraphs.append(createRandomGraph(numberOfVertices, numberOfEdges))
        self.__indexOfCurrentGraph = len(self.__listOfGraphs) - 1
        print("Successfully!")

    def getNumberOfVertices(self):
        numberOfVertices = self.__listOfGraphs[self.__indexOfCurrentGraph].getNumberOfVertices
        print(f"Number of vertices of the current graph is: {numberOfVertices}")

    def getNumberOfEdges(self):
        numberOfEdges = self.__listOfGraphs[self.__indexOfCurrentGraph].getNumberOfEdges
        print(f"Number of edges of the current graph is: {numberOfEdges}")

    def parseTheSetOfVertices(self):
        listOfAllVertices = []
        for vertex in self.__listOfGraphs[self.__indexOfCurrentGraph].parseSetOfVertices():
            listOfAllVertices.append(vertex)
        print(*listOfAllVertices)

    def verifyIfThereIsAnEdgeBetweenTwoVertices(self):
        sourceVertex = int(input("Enter source vertex: "))
        targetVertex = int(input("Enter target vertex: "))
        edgeFound = self.__listOfGraphs[self.__indexOfCurrentGraph].checkIfTheGraphHasGivenEdge(sourceVertex, targetVertex)
        if edgeFound:
            print(f"The edge ({sourceVertex}, {targetVertex}) exists!")
        else:
            print(f"The edge ({sourceVertex}, {targetVertex}) doesn't exist!")

    def getDegreeOfAVertex(self):
        givenVertex = int(input("Enter a vertex: "))
        degree = self.__listOfGraphs[self.__indexOfCurrentGraph].getInDegreeGivenVertex(givenVertex)
        print(f"The in degree of vertex {givenVertex} is: {degree}")

    def parseSetOfEdgesOfAVertex(self):
        listOfAllSuccessorsOfGivenVertex = []
        givenVertex = int(input("Enter a vertex: "))
        for successor in self.__listOfGraphs[self.__indexOfCurrentGraph].parseSetOfEdgesOfAVertex(givenVertex):
            listOfAllSuccessorsOfGivenVertex.append(successor)
        print(*listOfAllSuccessorsOfGivenVertex)

    def addVertex(self):
        newVertex = int(input("Enter the new vertex: "))
        self.__listOfGraphs[self.__indexOfCurrentGraph].addNewVertex(newVertex)
        print("Successfully!")

    def removeVertex(self):
        vertexToDelete = int(input("Enter the vertex: "))
        self.__listOfGraphs[self.__indexOfCurrentGraph].removeVertex(vertexToDelete)
        print("Successfully!")

    def addEdge(self):
        print("Add an edge, provide source vertex and target vertex: ")
        sourceVertex = int(input("Source vertex: "))
        targetVertex = int(input("Target vertex: "))
        if self.__listOfGraphs[self.__indexOfCurrentGraph].addNewEdge(sourceVertex, targetVertex):
            print("Successfully!")
        else:
            print("Edge already exists!")

    def removeEdge(self):
        sourceVertex = int(input("Source vertex: "))
        targetVertex = int(input("Target vertex: "))
        self.__listOfGraphs[self.__indexOfCurrentGraph].removeAnEdge(sourceVertex, targetVertex)
        print("Successfully!")

    def createACopyOfTheGraph(self):
        copyOfTheGraph = deepcopy(self.__listOfGraphs[self.__indexOfCurrentGraph])
        self.__listOfGraphs.append(copyOfTheGraph)
        self.__indexOfCurrentGraph = len(self.__listOfGraphs) - 1
        print("Successfully!")

    def readGraphFromTextFile(self):
        textFileName = input("Enter a valid file name to read from: ")
        self.__listOfGraphs.append(readGraphFromTextFile(textFileName))
        self.__indexOfCurrentGraph = len(self.__listOfGraphs) - 1
        print("Successfully!")

    def writeGraphToTextFile(self):
        textFileName = input("Enter a file name: ")
        writeGraphToTextFile(textFileName, self.__listOfGraphs[self.__indexOfCurrentGraph])
        print("Successfully!")

    def createAnEmptyGraph(self):
        emptyGraph = UndirectedGraph(0, 0)
        self.__listOfGraphs.append(emptyGraph)
        self.__indexOfCurrentGraph = len(self.__listOfGraphs) - 1

    def switchCurrentGraph(self):
        print(f"You can choose a graph from existing graphs(0 - {len(self.__listOfGraphs) - 1}), index of current graph is: {self.__indexOfCurrentGraph}")
        newIndex = int(input("New index: "))
        if newIndex >= len(self.__listOfGraphs) or newIndex < 0:
            raise ValueError("Invalid index!")
        self.__indexOfCurrentGraph = newIndex
        print("Successfully!")

    def findConnectedComponentsOfGraph(self):
        connectedComponents = self.__listOfGraphs[self.__indexOfCurrentGraph].findConnectedComponents()
        print(*connectedComponents)

    @staticmethod
    def displayMenu():
        print("Menu:")
        print("\t1. Add a vertex.")
        print("\t2. Remove a vertex.")
        print("\t3. Add an edge.")
        print("\t4. Remove an edge.")
        print("\t5. Get the number of vertices.")
        print("\t6. Get the number of edges.")
        print("\t7. Parse the set of vertices.")
        print("\t8. Verify if there is an edge between two vertices.")
        print("\t9. Get the degree of a vertex.")
        print("\t10. Parse the set of edges of a vertex.")
        print("\t11. Create a random graph with specified number of vertices and of edges.")
        print("\t12. Make a copy of the graph.")
        print("\t13. Read a graph from a text file.")
        print("\t14. Write the graph in a text file.")
        print("\t15. Switch between existing graphs.")
        print("\t16. Find all connected components of the graph using breadth first.")
        print("\t0. Exit.")


    def start(self):
        self.createAnEmptyGraph()
        while True:
            self.displayMenu()
            userOption = input("Enter an option: ")
            if userOption == '0':
                break
            elif userOption in self.__allCommands:
                try:
                    self.__allCommands[userOption]()
                except ValueError as errorMessage:
                    print("--- try again --- " + str(errorMessage))
                except IOError as errorMessage:
                    print("--- try again --- " + str(errorMessage))
                except GraphError as errorMessage:
                    print("--- try again --- " + str(errorMessage))
            else:
                print("Invalid command!")