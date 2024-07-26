# Créez un programme qui affiche son nom de fichier.


# Exemples d’utilisation :
# $> node exo.js
# exo.js

# $> node crevette.js
# crevette.js


import sys

program_name: str = sys.argv[0]
print(program_name)
