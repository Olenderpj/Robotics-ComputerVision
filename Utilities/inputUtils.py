options = ["Y", "N"]

def getUserChoice():
    choice = input("Do you want to generate a map?\n-->")
    while choice.upper() not in options:
        choice = input("Do you want to generate a map?\n-->")

    return choice.upper()

