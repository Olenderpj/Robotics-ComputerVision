import logging

from Constants.youBotConstants import *
from Constants.EnvironmentConstants import *
from Utilities.mathUtils import *
from Utilities.loggingUtils import *


class YouBot:

    def __init__(self, sim, agentConstantPath=YOUBOT):
        self.sim = sim
        self.entityHandle = self.sim.getObject(YOUBOT)
        self.floorHandle = self.sim.getObject(FLOOR)
        self.frontLeftMotor = self.sim.getObject(YOUBOT_ROLLING_JOINT_FL)
        self.frontRightMotor = self.sim.getObject(YOUBOT_ROLLING_JOINT_FR)
        self.rearLeftMotor = self.sim.getObject(YOUBOT_ROLLING_JOINT_RL)
        self.rearRightMotor = self.sim.getObject(YOUBOT_ROLLING_JOINT_RR)
        self.maximumVelocity = 2.0

    def setFrontLeftMotorVelocity(self, velocity):
        self.sim.setJointTargetVelocity(self.frontLeftMotor, velocity)

    def setFrontRightMotorVelocity(self, velocity):
        self.sim.setJointTargetVelocity(self.frontRightMotor, velocity)

    def setRearLeftMotorVelocity(self, velocity):
        self.sim.setJointTargetVelocity(self.rearLeftMotor, velocity)

    def setRearRightMotorVelocity(self, velocity):
        self.sim.setJointTargetVelocity(self.rearRightMotor, velocity)

    def setAllMotorsToSameVelocity(self, velocity):
        self.sim.setJointTargetVelocity(self.frontLeftMotor, velocity)
        self.sim.setJointTargetVelocity(self.frontRightMotor, velocity)
        self.sim.setJointTargetVelocity(self.rearLeftMotor, velocity)
        self.sim.setJointTargetVelocity(self.rearRightMotor, velocity)

    def stop(self):
        self.sim.setJointTargetVelocity(self.frontLeftMotor, 0)
        self.sim.setJointTargetVelocity(self.frontRightMotor, 0)
        self.sim.setJointTargetVelocity(self.rearLeftMotor, 0)
        self.sim.setJointTargetVelocity(self.rearRightMotor, 0)

    """ Left = 0, Right = 1"""
    def moveToAngle(self, targetAngle, direction=0, velocity=.2):
        if velocity > self.maximumVelocity:
            velocity = self.maximumVelocity

        if direction > 1:
            logging.warning("Invalid direction choice, defaulted to 0")
            direction = 0

        if direction == 0:
            self.sim.setJointTargetVelocity(self.frontLeftMotor, velocity)
            self.sim.setJointTargetVelocity(self.frontRightMotor, -velocity)
            self.sim.setJointTargetVelocity(self.rearLeftMotor, velocity)
            self.sim.setJointTargetVelocity(self.rearRightMotor, -velocity)
        else:
            self.sim.setJointTargetVelocity(self.frontLeftMotor, -velocity)
            self.sim.setJointTargetVelocity(self.frontRightMotor, velocity)
            self.sim.setJointTargetVelocity(self.rearLeftMotor, -velocity)
            self.sim.setJointTargetVelocity(self.rearRightMotor, velocity)

        initialEntityPosition = mapEntityOrientationFromRadiansToDegrees(self.getEntityAngle())
        targetValues = [abs(math.ceil(initialEntityPosition[1] - targetAngle)) % 180,
                        abs(math.ceil(initialEntityPosition[1] + targetAngle)) % 180]

        while True:
            currentEntityAngleDegrees = mapEntityOrientationFromRadiansToDegrees(self.getEntityAngle())
            currentAngle = math.ceil(currentEntityAngleDegrees[1] % 180)
            message = f"CURRENT: {currentAngle} Target: {targetValues}"
            logMessageToSim(self.sim, message)

            if currentAngle in targetValues or currentAngle % 180 in targetValues:
                self.stop()
                break

    # roll = x, pitch = y, yaw = z
    def getEntityAngle(self):
        orientation = self.sim.getObjectOrientation(self.entityHandle, self.floorHandle)
        return orientation

    def readProximitySensor1(self):

        sensorHandle = self.sim.getObject(YOUBOT_PROXIMITY_SENSOR_1)
        sensorReading = self.sim.handleProximitySensor(self.sim.handle_all_except_explicit)
        print(sensorReading)




