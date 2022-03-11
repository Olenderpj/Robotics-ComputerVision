from Constants.EnvironmentConstants import *
from Constants.OutputConstants import SHAPE_FILL
import matplotlib.pyplot as plt
import numpy as np


def buildPlot(sim):
    """
    Build the base plot object with using the eulerian coordinates
    :param sim:
    :return:
    """
    plot = plt
    floor = sim.getObject(FLOOR)
    floorBoundingBox = sim.getShapeBB(floor)
    floorXY = [-floorBoundingBox[0] / 2, floorBoundingBox[1] / 2]

    plot.xlim(floorXY)
    plot.ylim(floorXY)

    return plot


def plotObstacles(plot, obstacles):
    for i in obstacles:
        if i.shapeName not in EXCLUDED_SCENE_OBJECTS:
            obstacle = plot.Rectangle([i.lowerLeftX, i.lowerLeftY], i.shapeWidth, i.shapeHeight, color=SHAPE_FILL)
            plot.gca().add_patch(obstacle)
    return plot


def plotNodes(plot, nodes):
    for i in nodes:
        print("Plotting: ", i)
        node = plot.Circle(i, radius=NODE_RADIUS, color=NODE_COLOR)
        plot.gca().add_patch(node)

    return plot


def generateNodes(minX, maxX, minY, maxY):
    nodeArray = []

    for y in np.arange(minY, maxY + NODE_SPACING + 2, NODE_SPACING):
        for x in np.arange(minX, maxX + NODE_SPACING + 2, NODE_SPACING):
            print("X: ", round(x, 8), "Y:", round(y, 8))
            node = (y, x)

            nodeArray.append(node)
    return nodeArray


def evaluateAllNodes(nodeArray, obstacleArray):
    invalidNodeArray = []

    print(len(nodeArray))
    for node in nodeArray:
        x, y = node
        for obstacle in obstacleArray:
            a = obstacle.lowerLeftX < x < obstacle.upperRightX
            b = obstacle.lowerLeftY < y < obstacle.upperRightY

            if a and b:
                invalidNodeArray.append(node)

    print(len(invalidNodeArray))
    return invalidNodeArray


def cleanNodes(invalidNodes, allNodes):
    nodes = []
    for i in range(len(allNodes)):
        if allNodes[i] not in invalidNodes:
            nodes.append(allNodes[i])
    return nodes


