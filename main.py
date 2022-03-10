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
    obstacles = getAllShapeObjects(sim)
    plot = plotObstacles(plot, obstacles)
    plot.show()

    stopSimulation(sim)


if __name__ == "__main__":
    main()
