
from Controllers.youBot import YouBot
from Utilities import simulationUtils
from Constants.EnvironmentConstants import *
from time import sleep

from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient

from PIL import Image, ImageDraw

client = RemoteAPIClient()
sim = client.getObject('sim')

simulationUtils.stopSimulation(sim)

clientID = simulationUtils.startSimulation(sim)

#simulationShapes = simulationUtils.getAllShapeObjects(sim, 1000)


if __name__ == "__main__":
    floor = sim.getObject(FLOOR)
    obj = sim.getObject("/240cmHighPillar50cm")
    objPos = sim.getObjectPosition(obj, floor)
    shapeBB = sim.getShapeBB(floor)
    print("Obj pos:", objPos)
    print("Floor BB:", shapeBB)

    # img = Image.new(mode="RGB", size=(int(shapeBB[0] * 100),int(shapeBB[1] * 100) ))
    # img1 = ImageDraw.Draw(img)
    # shape = [(40, 40), (100, 100)]
    # img1.rectangle(shape, fill="white")
    # img.show()

    img = Image.new(mode="RGB", size=(int(shapeBB[0] * 100), int(shapeBB[1] * 100)))
    img1 = ImageDraw.Draw(img)
    shape = [(40, 40), (100, 100)]
    img1.rectangle(shape, fill="white")
    img.show()



    simulationUtils.stopSimulation(sim)
