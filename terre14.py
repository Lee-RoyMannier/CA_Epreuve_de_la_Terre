# Créez un programme qui détermine si une liste d’entiers est triée ou pas.


# Exemples d’utilisation :
# $> ruby exo.rb 9 8 3
# Pas triée !

# $> ruby exo.rb 3 8 9 12
# Triée !

# $> ruby exo.rb “Salut”
# erreur.


# Fonctions interdites: 
# -La fonction sort


import sys


def is_num(n: str):
    for i in n:
        return ord(i) < 48 or ord(i) > 57


def is_sort(values: list):
    c: int = 0
    i: int = 0

    while i < len(values) -1 :
        if is_num(values[i]):
            return "erreur"

        if int(values[i]) > int(values[i + 1]):
            c += 1
        else:
            c -= 1

        i += 1

    if c == len(values) - 1:
        return "Pas Triée !"

    return "Triée !"


if len(sys.argv[1:]) < 2:
    print("Erreur")
    sys.exit()

print(is_sort(sys.argv[1:]))