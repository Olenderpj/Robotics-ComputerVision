import logging
import time
from Utilities.loggingUtils import *
from Constants.EnvironmentConstants import EXCLUDED_SCENE_OBJECTS
from ObjectClasses.SceneShape import SceneShape
from Utilities.loggingUtils import printSuccessMessage


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
    allSimulationShapeObjects = []
    i = 0
    print("Getting all simulation shapes")

    while i < estimatedSceneShapes:
        objectHandle = simulation.getObjects(i,  simulation.object_shape_type)
        if objectHandle != -1:
            printRetrievalMessage(f"[Retrieval]: Retrieving object {objectHandle} from the Scene")
            shape = SceneShape(simulation, objectHandle)
            allSimulationShapeObjects.append(shape)
        else:
            break
        i += 1
    return allSimulationShapeObjects