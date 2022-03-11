from colorama import Fore, Back, Style


def printSuccessMessage(message):
    print(Fore.GREEN + message, Style.RESET_ALL)


def printBuildMessage(message):
    print(Fore.BLUE + message, Style.RESET_ALL)


def printNodeMessage(message):
    print(Fore.LIGHTGREEN_EX + message, Style.RESET_ALL)


def printRetrievalMessage(message):
    print(Fore.YELLOW + message, Style.RESET_ALL)


def logErrorToSim(simulation, message):
    simulation.addLog(simulation.verbosity_errors, message)


def logMessageToSim(simulation, message):
    simulation.addLog(simulation.verbosity_default, message)
