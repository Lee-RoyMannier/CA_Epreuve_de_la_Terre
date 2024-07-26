# Créez un programme qui affiche le résultat d’une puissance.


# L’exposant ne pourra pas être négatif.


# Exemples d’utilisation :
# $> node exo.js 2 3
# 8

# Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


# Fonctions interdites:
# -La fonction pow


import sys


def is_pos(n):
    if n > 0:
        return True
    return False


def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


a, n = int(sys.argv[1]), int(sys.argv[2])

if is_pos(n):
    print(power(a, n))
else:
    print("Invalid input")
