from Utilities import simulationUtils
from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient
from ObjectClasses.PixelMap import PixelMap
from PIL import Image
import numpy as np
from PathFinding.Dijkstras import Dijkstras



if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    simulationUtils.stopSimulation(sim)
    clientID = simulationUtils.startSimulation(sim)

    # Build the Pixel map from the simulation environment
    #pixelMap = PixelMap(sim)
    # pixelMap.buildBWPixelMap()

    import sys
    import numpy

    numpy.set_printoptions(threshold=sys.maxsize)

    image = Image.open("SceneMaps/Maze.png")
    imageArray = np.array(image)

    print(len(imageArray[500]))



    simulationUtils.stopSimulation(sim)
