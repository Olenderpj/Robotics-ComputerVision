import math


class PlotShape:

    def __init__(self, simulation, shapeHandle, floorHandle):
        self.simHandle = simulation
        self.shapeHandle = shapeHandle
        self.floorHandle = floorHandle
        self.orientation = round(math.degrees(simulation.getObjectOrientation(shapeHandle, self.floorHandle)[2]))
        self.shapeName = simulation.getObjectAlias(shapeHandle)
        self.shapeBoundingBox = simulation.getShapeBB(shapeHandle)
        self.shapePos = simulation.getObjectPosition(shapeHandle, floorHandle)

        # Objects Height and width dimensions used for generatring the pygame square
        # Object is on the horizontal plane
        if self.orientation == 90 or self.orientation == -90:
            self.shapeWidth = self.shapeBoundingBox[1]
            self.shapeHeight = self.shapeBoundingBox[0]

        # Object is on the vertical plane
        elif self.orientation == 0 or self.orientation == -180 or self.orientation == 180:
            self.shapeWidth = self.shapeBoundingBox[0]
            self.shapeHeight = self.shapeBoundingBox[1]

        self.lowerLeftX = self.shapePos[0] - (self.shapeWidth * .5)
        self.lowerLeftY = self.shapePos[1] - (self.shapeHeight * .5)


    def __str__(self):
        return "\nHandle: " + str(self.shapeHandle) + \
               "\n\tName: " + self.shapeName +\
               "\n\tOrientation: " + str(self.orientation) +\
               "\n\tLL X:" + str(self.lowerLeftX) +\
               "\n\tLL Y:" + str(self.lowerLeftY) +\
               "\n\tWidth:" + str(self.shapeWidth) +\
               "\n\tHeight:" + str(self.shapeHeight)
