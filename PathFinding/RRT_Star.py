import math
import random

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
        self.nodeRadius = 2
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

    def addNode(self, n, x, y):
        self.x.insert(n, x)
        self.y.append(y)

    def removeNode(self, n):
        self.x.pop(n)
        self.y.pop(n)

    def addEdge(self, parent, child):
        self.parent.insert(child, parent)

    def removeEdge(self, n):
        self.parent.pop(n)

    def numberOfNodes(self):
        return len(self.x)

    def distance(self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        px = (float(x1) - float(x2)) ** 2
        py = (float(y1) - float(y2)) ** 2

        return (px + py) ** (0.5)

    def sampleEnvironment(self):
        x = int(random.uniform(0, self.mapWidth))
        y = int(random.uniform(0, self.mapHeight))
        return x, y

    def nearest(self):
        pass

    def isFree(self):
        n = self.numberOfNodes() - 1
        (x, y) = (self.x[n], self.y[n])
        obstacles = self.obstacles.copy()
        while len(obstacles) > 0:
            rectangle = obstacles.pop(0)
            if rectangle.collidepoint(x, y):
                self.removeNode(n)
                return False
        return True

    def crossObstacle(self, x1, x2, y1, y2):
        obstacle = self.obstacles.copy()
        while len(obstacle) > 0:
            rectangle = obstacle.pop(0)
            for i in range(0, 101):
                u = i / 100
                x = x1 * u + x2*(1-u)
                y = y1 * u + y2*(1-u)
                if rectangle.collidepoint(x, y):
                    return True
        return False

    def connect(self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        if self.crossObstacle(x1, x2, y1, y2):
            self.removeNode(n2)
            return False
        else:
            self.addEdge(n1, n2)
            return True

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



