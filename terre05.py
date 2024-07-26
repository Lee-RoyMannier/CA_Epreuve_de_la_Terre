# Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.


# Exemples d’utilisation :
# $> python exo.py 5 2
# résultat: 2
# reste: 1


# $> python exo.py 10 0
# erreur.


# $> python exo.py 3 5
# erreur.


import sys
from typing import Tuple


def divide(a: int, b: int):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    elif a < b:
        raise ValueError("Dividend should be greater than divisor")

    result: int = a // b
    mod: int = a % b
    return result, mod


a, b = int(sys.argv[1]), int(sys.argv[2])
result, mod = divide(a, b)
print(f"result: {result}\nmod: {mod}")
