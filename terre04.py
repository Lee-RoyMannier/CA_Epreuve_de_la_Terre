# Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..


# Exemples d’utilisation :
# $> ruby exo.rb 2
# pair

# $> ruby exo.rb 5
# impair


# $> ruby exo.rb Bonjour
# Tu ne me la mettras pas à l’envers.

# $> ruby exo.rb
# Tu ne me la mettras pas à l’envers.


# Attention : gérez aussi les entiers négatifs.

# Fonctions interdites:
# -En Ruby: even? et odd?


import sys


def even_odd(n: int) -> str:
    if ord(chr(n)) < 48 or ord(chr(n)) > 57:
        return "Invalid input"

    if n % 2 == 0:
        return "Even"
    return "Odd"


args = int(sys.argv[1])
print(even_odd(args))
