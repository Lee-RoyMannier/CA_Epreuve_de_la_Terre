# Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.


# Exemples d’utilisation :
# $> node exo.js “Hello world!@”
# @!dlrow olleH


# $> node exo.js “lehciM”
# Michel

# Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


# Fonctions interdites:
# -La fonction reverse


import sys


def len(string: list[str]) -> int:
    length: int = 0
    try:
        while True:
            _ = string[length]
            length += 1
    except IndexError:
        pass

    return length


def reverse_str(string: str, len) -> None:
    start = len(string) - 1
    end = 0

    while start >= end:
        print(string[start], end="")
        start -= 1

    print("\n")


string: str = sys.argv[1]
reverse_str(string, len)
