from Utilities import simulationUtils
from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient
from Utilities.simulationUtils import *
from Utilities.inputUtils import getUserChoice, options
from Utilities.PlotUtilities import *


def main():
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    simulationUtils.stopSimulation(sim)
    clientID = simulationUtils.startSimulation(sim)

    # if getUserChoice() == "Y":
    #    # Build the Pixel map from the simulation environment
    #    pixelMap = PixelMap(sim, sceneShapes)
    #    pixelMap.buildBWPixelMap()

    plot = buildPlot(sim)
    plot.title("Maze Map")
    obstacles = getAllShapeObjects(sim)
    plot = plotObstacles(plot, obstacles)

    minX, maxX, minY, maxY = getMinMax(obstacles)

    print(minX, maxX, minY, maxY)

    generatedNodes = generateNodes(minX, maxX, minY, maxY)
    invalidNodes = evaluateAllNodes(generatedNodes, obstacles)
    goodNodes = cleanNodes(invalidNodes, generatedNodes)
    plot = plotNodes(plot, goodNodes)
    plot.show()


    # I think that this adjactency list could work, I just have to make a 2d array from the existing normal array
    #https://www.programiz.com/dsa/graph-adjacency-list
        # from PathFinding.Graph import Graph
        # v = len(goodNodes)
        # 
        # graph = Graph(v)
        # for i in goodNodes:
        #     x, y = i
        #     graph.add_edge(x, y)
        # 
        # graph.print_agraph()
        # 
        # stopSimulation(sim)



if __name__ == "__main__":
    main()
