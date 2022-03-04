from Utilities import simulationUtils
from Constants.EnvironmentConstants import *
from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient
from ObjectClasses.PixelMap import PixelMap


if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.getObject('sim')

    simulationUtils.stopSimulation(sim)

    clientID = simulationUtils.startSimulation(sim)

    floor = sim.getObject(FLOOR)

    print(sim.getShapeBB(floor))

    pixelMap = PixelMap(sim)
    print(pixelMap.floorPixelsX, pixelMap.floorPixelsY)
    pixelMap.buildBWPixelMap()

    #img1.rectangle([(sc.pixelValues.drawX1, sc.pixelValues.drawY1), (sc.pixelValues.drawX2, sc.pixelValues.drawY2)], fill="white")
    #img2.rectangle([(scc.pixelValues.drawX1, scc.pixelValues.drawY1), (scc.pixelValues.drawX2, scc.pixelValues.drawY2)], fill="Blue")
    #img.show()

    simulationUtils.stopSimulation(sim)
