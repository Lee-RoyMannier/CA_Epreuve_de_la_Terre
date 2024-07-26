# Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.


# Exemples d’utilisation :
# $> ruby exo.rb 11 40 34
# 34

# $> ruby exo.rb 2 1 3
# 2

# $> ruby exo.rb 2 2 2
# erreur.


# Fonctions interdites: 
# -La fonction sort
# # 

import sys

def min(values: list):
    min_v = values[0]
    i: int = 0

    while i <= len(values) - 1:
        if values[i] < min_v:
            min_v = values[i]
        
        i += 1
    
    return min_v



def max(values: list):
    max_v = values[0]
    i: int = 0

    while i < len(values):
        if values[i] > max_v:
            max_v = values[i]
        
        i += 1
    
    return max_v


def middle(values: list):
    max_v: int = max(values)
    min_v: int = min(values)
    i: int = 0

    while i < len(values):
        if values[i] is not max(values) and values[i] is not min(values):
            return values[i]
        i += 1
    return "Erreur"

print(middle(sys.argv[1:]))