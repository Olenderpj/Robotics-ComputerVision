from Utilities.loggingUtils import *
from Constants.OutputConstants import *
from Constants.EnvironmentConstants import *
from Utilities.simulationUtils import getAllShapeObjects
from PIL import Image, ImageDraw


class PixelMap:
    """
    Collects all object within the scene using a helper utility method and then plots all
    Shape objects within the scene to a black and white image.
    """

    def __init__(self, simulation):
        self.sceneShapes = getAllShapeObjects(simulation)
        self.floorHandle = simulation.getObject(FLOOR)
        self.floorBoundingBox = simulation.getShapeBB(self.floorHandle)
        self.floorPixelsX = int(self.floorBoundingBox[0] * PIXEL_SCALAR)
        self.floorPixelsY = int(self.floorBoundingBox[1] * PIXEL_SCALAR)

    def buildBWPixelMap(self):
        baseImage = Image.new(mode=COLOR_MODE, size=(self.floorPixelsX, self.floorPixelsY), color=BG_COLOR)

        for shape in self.sceneShapes:
            if shape.name not in EXCLUDED_SCENE_OBJECTS:
                printBuildMessage(f"[BUILD]: Building {shape.objectHandle}, {shape.name}")
                shapeToAdd = ImageDraw.Draw(baseImage)
                shapeToAdd.rectangle([(shape.pixelValues.drawX1,
                                       shape.pixelValues.drawY1),
                                      (shape.pixelValues.drawX2,
                                       shape.pixelValues.drawY2)],
                                     fill=SHAPE_FILL)

        print(f"[PHOTO SHAPE]: {self.floorPixelsX} x {self.floorPixelsY}")
        baseImage.show()
        baseImage.save("SceneMaps/Maze.png")
