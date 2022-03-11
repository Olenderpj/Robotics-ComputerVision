import logging
import time
from Utilities.loggingUtils import *
from ObjectClasses.PlotShape import PlotShape
from Utilities.loggingUtils import printSuccessMessage
from Constants.EnvironmentConstants import *

def stopSimulation(simulation):
    try:
        simulation.stopSimulation()
        time.sleep(.25)
    except:
        logging.warning("[ERROR]: An error occurred while attempting to stop the simulation environment")


def startSimulation(simulation):
    try:
        sim = simulation.startSimulation()
        time.sleep(.25)
        message = "Simulation was started successfully with ID: " + str(sim)
        printSuccessMessage(message)
        return sim
    except:
        logging.warning("[ERROR]: An error occurred while attempting to start the simulation environment")


# Get all shape objects from the simulation scene - Things like walls, pillars, etc
def getAllShapeObjects(simulation, estimatedSceneShapes=1500):
    """
    Retrieve all shape objects from the scene and build PlotShape Objects
    :param simulation:
    :param estimatedSceneShapes:
    :return: list of simulation objects:
    """
    # Get the floor handle here because it saves computation power when creating shape objects
    floorHandle = simulation.getObjectHandle(FLOOR)

    allSimulationShapeObjects = []
    i = 0

    while i < estimatedSceneShapes:
        objectHandle = simulation.getObjects(i,  simulation.object_shape_type)
        if objectHandle != -1:
            printRetrievalMessage(f"[Retrieval]: Retrieving object {objectHandle} from the Scene")
            shape = PlotShape(simulation, objectHandle, floorHandle)
            print(shape)
            if shape.shapeName not in EXCLUDED_SCENE_OBJECTS:
                allSimulationShapeObjects.append(shape)
        else:
            break
        i += 1
    return allSimulationShapeObjects


def getMinMax(array):
    minX, maxX, minY, maxY = 0, 0, 0, 0

    for i in array:
        if i.lowerLeftX > maxX:
            maxX = i.lowerLeftX

        if i.lowerLeftX < minX:
            minX = i.lowerLeftX

        if i.lowerLeftY > maxY:
            maxY = i.lowerLeftY

        if i.lowerLeftY < minY:
            minY = i.lowerLeftY

    return minX, maxX, minY, maxY

