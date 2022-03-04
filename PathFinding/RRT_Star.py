import math
import pygame
from Utilities.loggingUtils import *
from Constants.EnvironmentConstants import *
from Utilities.simulationUtils import getAllShapeObjects


class RRTMap:
    def __init__(self, simulation, start, goal, width, height, sceneShapes):
        self.simulation = simulation
        self.sceneShapes = sceneShapes
        self.start = start
        self.goal = goal
        self.mapWidth = width
        self.mapHeight = height

        # Pygame window settings
        self.mapWindowName = "RRT Path Planning"
        pygame.display.set_caption(self.mapWindowName)
        self.map = pygame.display.set_mode((self.mapWidth, self.mapHeight))
        self.map.fill((255,255,255))
        self.nodeRadius = 0
        self.nodeThickness = 0
        self.edgeThickness = 1

        self.obstacles = []

        # Initialize some Color Values
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

    def drawMap(self, obstacles):
        pygame.draw.circle(self.map, self.green, self.start, self.nodeRadius + 5, 0)
        pygame.draw.circle(self.map, self.red, self.goal, self.nodeRadius + 20, 1)
        self.drawObstacles(obstacles)

    def drawPath(self):
        pass

    def drawObstacles(self, obstacles):
        obstacleList = obstacles.copy()
        while (len(obstacleList)) > 0:
            obstacle = obstacleList.pop(0)
            printSuccessMessage(f"[SUCCESS]: Drawing pygame Object {obstacle}")
            pygame.draw.rect(self.map, self.grey, obstacle)


class RRTGraph:
    def __init__(self, simulation, start, goal, width, height, sceneShapes):
        self.simulation = simulation
        self.sceneShapes = sceneShapes
        (x, y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False
        self.mapWidth = width
        self.mapHeight = height

        # define lists of empty nodes
        self.x = []
        self.y = []
        self.parent = []

        # Initialize the tree structure
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)

        # Obstacles
        self.obstacles = []

        # Path
        self.goalState = None
        self.path = []

    def makeObstacles(self):
        obstacles = []
        allShapes = self.sceneShapes

        for i in allShapes:
            if i.name not in EXCLUDED_SCENE_OBJECTS:
                printBuildMessage(f"[BUILD]: Building Pygame Objects - {i.objectHandle}, {i.name}")
                print(i.name, "X:", i.pixelCoordinates.drawX2,
                      "Y:", i.pixelCoordinates.drawY2)
                obj = pygame.Rect(i.pixelCoordinates.drawX1,
                                  i.pixelCoordinates.drawY2,
                                  i.shapeBoundingBoxWidth,
                                  i.shapeBoundingBoxHeight)
                obstacles.append(obj)

        self.obstacles = obstacles.copy()

        return obstacles

    def addNode(self):
        pass

    def removeNode(self):
        pass

    def addEdge(self):
        pass

    def removeEdge(self):
        pass

    def numberOfNodes(self):
        pass

    def distance(self):
        pass

    def nearest(self):
        pass

    def isFree(self):
        pass

    def crossObstacle(self):
        pass

    def connect(self):
        pass

    def step(self):
        pass

    def pathToGoal(self):
        pass

    def getPathCoords(self):
        pass

    def bias(self):
        pass

    def expand(self):
        pass

    def cost(self):
        pass



