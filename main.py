from Controllers.youBot import YouBot
from Utilities import simulationUtils
from time import sleep

from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
simulation = client.getObject('sim')

simulationUtils.stopSimulation(simulation)

clientID = simulationUtils.startSimulation(simulation)

youBot = YouBot(simulation)

youBot.setAllMotorsToSameVelocity(5)

while True:
    youBot.readProximitySensor1()


sleep(3)

sleep(4)

simulationUtils.stopSimulation(simulation)
