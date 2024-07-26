# Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.


# Exemples d’utilisation :
# $> python exo.py “Hello world!”
# 12


# $> python exo.py
# erreur.


# $> python exo.py “Bonjour” “Aurevoir”
# erreur.

# $> python exo.py 10
# erreur.


# Fonctions interdites:
# -La fonction length
# -La fonction size


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


if len(sys.argv[1:]) > 1:
    print("erreur")
    sys.exit()

print(len(list(sys.argv[1])))
