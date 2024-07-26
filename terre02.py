# Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.


# Exemples d’utilisation :
# $> ruby exo.rb je suis solide !
# je
# suis
# solide
#


import sys


def len(arguments: list[str]) -> int:
    length: int = 0
    try:
        while True:
            _ = arguments[length]
            length += 1
    except IndexError:
        pass

    return length


i: int = 0
arguments: list[str] = sys.argv[1:]

while i <= len(arguments) - 1:
    print(arguments[i])
    i += 1
