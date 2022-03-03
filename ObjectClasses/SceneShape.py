from Constants.EnvironmentConstants import FLOOR


class SceneShape:

    def __init__(self, simulation, objectHandle):
        self.simulation = simulation
        self.floorHandle = simulation.getObject(FLOOR)
        self.objectHandle = objectHandle
        self.name = simulation.getObjectAlias(objectHandle, -1)
        self.boundingBox = simulation.getShapeBB(objectHandle)
        # Object position Relative to the floor
        self.objectPosition = simulation.getObjectPosition(self.objectHandle, self.floorHandle)

    def __str__(self):
        return "ID: " + str(self.objectHandle) + " Name: " + self.name
