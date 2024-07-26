# Créez un programme qui affiche si un nombre est premier ou pas.


# Exemples d’utilisation :
# $> node exo.js 5
# Oui, 5 est un nombre premier.

# $> node exo.js 6
# Non, 6 n’est pas un nombre premier.

# Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.


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


def is_prime(n: int):
    if n < 2:
        return f"{n} is not prime"

    i = 2
    while i < n:
        if n % i == 0:
            return f"{n} is not prime"
        i += 1

    return f"{n} is prime"


if len(sys.argv[1:]) > 1:
    print("erreur")
    sys.exit()

print(is_prime(int(sys.argv[1])))
