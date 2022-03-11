from Constants.EnvironmentConstants import *
from Utilities.loggingUtils import *
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
    """
    Plot all obstacles within an array as a square.
    :param plot:
    :param obstacles:
    :return:
    """
    for i in obstacles:
        if i.shapeName not in EXCLUDED_SCENE_OBJECTS:
            obstacle = plot.Rectangle([i.lowerLeftX, i.lowerLeftY], i.shapeWidth, i.shapeHeight, color=SHAPE_FILL)
            plot.gca().add_patch(obstacle)
    return plot


def plotNodes(plot, nodes):
    """
    Plot all nodes within an array
    :param plot:
    :param nodes:
    :return:
    """
    for i in nodes:
        printNodeMessage(f"Plotting: {i}")
        node = plot.Circle(i, radius=NODE_RADIUS, color=NODE_COLOR)
        plot.gca().add_patch(node)
    return plot


def generateNodes(minX, maxX, minY, maxY):
    """
    Generate All nodes within the x and y constraints at an interval set in the Environment constants file.
    :param minX:
    :param maxX:
    :param minY:
    :param maxY:
    :return:
    """
    nodeArray = []
    minXBounds = minX + NODE_SPACING
    minYBounds = minY + NODE_SPACING
    maxXBounds = maxX - (NODE_SPACING * .5)
    maxYBounds = maxY + (NODE_SPACING * .5)

    for y in np.arange(minYBounds, maxYBounds, NODE_SPACING):
        for x in np.arange(minXBounds, maxXBounds, NODE_SPACING):
            printNodeMessage(f"Generated Node at X: {round(x, 4)} Y: {round(y, 4)}")
            node = (y, x)

            nodeArray.append(node)
    return nodeArray


def evaluateAllNodes(nodeArray, obstacleArray):
    """
    Generate all of the invalid nodes within the maze
    :param nodeArray:
    :param obstacleArray:
    :return:
    """

    invalidNodeArray = []
    for node in nodeArray:
        x, y = node
        for obstacle in obstacleArray:
            # Evaluate the bounds of where each point resides
            if obstacle.lowerLeftX < x < obstacle.upperRightX and obstacle.lowerLeftY < y < obstacle.upperRightY:
                invalidNodeArray.append(node)
    return invalidNodeArray


def cleanNodes(invalidNodes, allNodes):
    """
    Remove all invalid nodes within the array
    :param invalidNodes:
    :param allNodes:
    :return:
    """
    nodes = []
    for i in range(len(allNodes)):
        if allNodes[i] not in invalidNodes:
            nodes.append(allNodes[i])
    return nodes
