from Constants.EnvironmentConstants import FLOOR, EXCLUDED_SCENE_OBJECTS
import matplotlib.pyplot as plt


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
            obstacle = plot.Rectangle([i.lowerLeftX, i.lowerLeftY], i.shapeWidth, i.shapeHeight)
            plot.gca().add_patch(obstacle)

    return plot
