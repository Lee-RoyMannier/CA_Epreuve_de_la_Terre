# Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.


# Exemples d’utilisation :
# $> python exo.py n
# nopqrstuvwxyz
# $>


# Attention : votre programme devra utiliser une boucle.


import sys


def print_alphabet(n) -> None:
    start: int = ord(n)
    end: int = 122
    i: int = 0

    while start <= end:
        i += 1
        print(chr(start), end="")
        start = ord(n) + i

    print("\n")


args = sys.argv[1]
print_alphabet(args)
