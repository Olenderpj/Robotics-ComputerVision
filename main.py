import sys
import numpy
import pygame
from Utilities import simulationUtils
from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient
from ObjectClasses.PixelMap import PixelMap
from Utilities.simulationUtils import getAllShapeObjects
from PIL import Image
import numpy as np

from PathFinding.RRT_Star import RRTGraph
from PathFinding.RRT_Star import RRTMap


def main():
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    simulationUtils.stopSimulation(sim)
    clientID = simulationUtils.startSimulation(sim)

    # Build the Pixel map from the simulation environment
    pixelMap = PixelMap(sim)
    #pixelMap.buildBWPixelMap()

    # numpy.set_printoptions(threshold=sys.maxsize)
    # image = Image.open("SceneMaps/Maze.png")
    # imageArray = np.array(image)
    # print(len(imageArray[500]))

    width = pixelMap.floorPixelsX
    height = pixelMap.floorPixelsY
    print("W:", width, " H:", height)
    start = (50, 50)
    goal = (75, 75)

    for i in getAllShapeObjects(sim):
        print(i.name)
        print(i.shapeBoundingBox)
        rectangleObj = pygame.Rect(i.pixelCoordinates.drawX1,
                                   i.pixelCoordinates.drawY1,
                                   i.shapeBoundingBox[0],
                                   i.shapeBoundingBox[1])
        print(rectangleObj)


    pygame.init()
    map = RRTMap(sim, start, goal, width, height)
    graph = RRTGraph(sim, start, goal, width, height)

    obstacles = graph.makeObstacles()
    map.drawMap(obstacles)

    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)

    simulationUtils.stopSimulation(sim)


if __name__ == "__main__":
    main()
