from colorama import Fore, Back, Style


def printSuccessMessage(message):
    print(Fore.GREEN + message, Style.RESET_ALL)


def logErrorToSim(simulation, message):
    simulation.addLog(simulation.verbosity_errors, message)


def logMessageToSim(simulation, message):
    simulation.addLog(simulation.verbosity_default, message)
