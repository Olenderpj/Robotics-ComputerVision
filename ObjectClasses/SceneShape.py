from Constants.EnvironmentConstants import FLOOR
from ObjectClasses.Pose import Pose
from ObjectClasses.PixelCoordinates import PixelCoordinates


class SceneShape:

    def __init__(self, simulation, objectHandle):
        self.simulation = simulation
        self.floorHandle = simulation.getObject(FLOOR)
        self.objectHandle = objectHandle
        self.name = simulation.getObjectAlias(objectHandle, -1)
        self.shapeBoundingBox = simulation.getShapeBB(objectHandle)
        self.floorBoundingBox = simulation.getShapeBB(self.floorHandle)
        # Object position Relative to the floor
        self.objectPosition = simulation.getObjectPosition(self.objectHandle, self.floorHandle)
        # Create a new pose object
        self.pose = Pose(self.simulation, self.objectHandle, self.floorHandle, self.shapeBoundingBox)
        self.pixelValues = PixelCoordinates(self.pose.x1,
                                            self.pose.y1,
                                            self.pose.x2,
                                            self.pose.y2,
                                            self.floorBoundingBox[0],
                                            self.floorBoundingBox[1])

    def __str__(self):
        return "ID: " + str(self.objectHandle) + " Name: " + self.name
