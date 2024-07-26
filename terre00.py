#     Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.


# Exemples d’utilisation :
# $> python exo.py
# abcdefghijklmnopqrstuvwxyz
# $>


# Attention : votre programme devra utiliser une boucle.


def print_alphabet() -> None:
    i: int = 97
    ns: str = ""

    while i <= 122:
        ns += chr(i)
        i += 1

    ns += "\n"

    print(ns)
