from Constants.OutputConstants import PIXEL_SCALAR
from Utilities.mathUtils import normalizePointValue


class PixelCoordinates:

    def __init__(self, x1, y1, x2, y2, maxX, maxY):

        self.lowerLeftX1 = normalizePointValue(x1, maxX) * PIXEL_SCALAR
        self.lowerLeftY1 = normalizePointValue(y1, maxY) * PIXEL_SCALAR
        self.lowerLeftX2 = normalizePointValue(x2, maxX) * PIXEL_SCALAR
        self.lowerLeftY2 = normalizePointValue(y2, maxY) * PIXEL_SCALAR
        self.drawX1 = self.lowerLeftX1
        self.drawY1 = (maxY * PIXEL_SCALAR) - self.lowerLeftY1
        self.drawX2 = self.lowerLeftX2
        self.drawY2 = (maxY * PIXEL_SCALAR) - self.lowerLeftY2

    def __str__(self):
        return "X1:" + str(self.drawX1) +\
               "\nY1:" + str(self.drawY1) +\
                "\nX2:" + str(self.drawX2) + \
                "\nY2:" + str(self.drawY2)
