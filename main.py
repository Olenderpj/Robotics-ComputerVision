from Controllers.youBot import YouBot
from Utilities import simulationUtils
from Constants.EnvironmentConstants import *
from time import sleep
from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient
from PIL import Image, ImageDraw
from ObjectClasses.SceneShape import SceneShape

client = RemoteAPIClient()
sim = client.getObject('sim')

simulationUtils.stopSimulation(sim)

clientID = simulationUtils.startSimulation(sim)

# simulationShapes = simulationUtils.getAllShapeObjects(sim, 1000)

if __name__ == "__main__":
    floor = sim.getObject(FLOOR)
    obj = sim.getObject("/240cmHighWall100cm")
    objPos = sim.getObjectPosition(obj, floor)
    objOri = sim.getObjectOrientation(obj, floor)
    floorPos = sim.getObjectPosition(floor, floor)
    shapeBB = sim.getShapeBB(obj)
    floorBB = sim.getShapeBB(floor)
    # print("Object BB: ", round(shapeBB[0], 3), round(shapeBB[1], 3), round(shapeBB[2], 3))
    # print("Object pos:", round(objPos[0], 3), round(objPos[1], 3), round(objPos[2], 3))
    # print("Object Orient:", objOri)
    # print("Floor BB:  ", round(floorBB[0], 3), round(floorBB[1], 3), round(floorBB[2], 3))
    # print("Floor pos: ", round(floorPos[0], 3), round(floorPos[1], 3), round(floorPos[2], 3))
    #print("Canvas: 5000 x 5000")

    # img = Image.new(mode="RGB", size=(int(shapeBB[0] * 100),int(shapeBB[1] * 100) ))
    # img1 = ImageDraw.Draw(img)
    # shape = [(40, 40), (100, 100)]
    # img1.rectangle(shape, fill="white")
    # img.show()

    from Utilities.mathUtils import normalizePointValue

    shapex = int(floorBB[0]) * 1000
    shapey = int(floorBB[1]) * 1000

    print("Shape:", shapex, shapey)
    sc = SceneShape(sim, obj)
    print(sc.pose.getValues())

    img = Image.new(mode="RGB", size=(shapex, shapey))
    img1 = ImageDraw.Draw(img)

    print(sc.pixelValues)


    img1.rectangle([sc.pixelValues.drawX1, sc.pixelValues.drawY1, sc.pixelValues.drawX2, sc.pixelValues.drawY2], fill="white")
    img.show()

    simulationUtils.stopSimulation(sim)
