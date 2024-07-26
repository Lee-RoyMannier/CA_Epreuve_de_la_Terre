# Créez un programme qui affiche la racine carrée d’un entier positif.


# Exemples d’utilisation :
# $> node exo.js 9
# 3

# Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


# Fonctions interdites:
# -La fonction sqrt

import sys


def len(arguments: list) -> int:
    length: int = 0
    try:
        while True:
            _ = arguments[length]
            length += 1
    except IndexError:
        pass

    return length


def sqrt(n: int, tol: float) -> float:
    if n < 0:
        return -1

    root = n

    while 1:
        diff = abs(n - root * root)
        if diff < tol:
            break
        root = (root + n / root) / 2

    return int(root)


if len(sys.argv[1:]) != 1:
    print("erreur")
    sys.exit()

print(sqrt(int(sys.argv[1]), 0.0001))
