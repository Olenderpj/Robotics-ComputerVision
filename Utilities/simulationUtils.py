import logging
import time
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
