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
    sceneShapes = getAllShapeObjects(sim)

    # Build the Pixel map from the simulation environment
    pixelMap = PixelMap(sim, sceneShapes)
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

    pygame.init()
    gameMap = RRTMap(sim, start, goal, width, height, sceneShapes)
    graph = RRTGraph(sim, start, goal, width, height, sceneShapes)

    obstacles = graph.makeObstacles()
    gameMap.drawMap(obstacles)

    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)

    simulationUtils.stopSimulation(sim)


if __name__ == "__main__":
    main()
