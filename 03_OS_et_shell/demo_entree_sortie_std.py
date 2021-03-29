#!/opt/tljh/user/bin/python

# la première ligne du fichier est spéciale:
#   on l'appelle «ligne shebang»
#   c'est nécessairement la toute première ligne du programme
#   elle débute obligatoirement par «#!»
#   et précise où se trouve l'interpréteur du langage du fichier
#   au final, si le fichier est déclaré exécutable,
#       ...$ <chemin_fichier>
#   lance ce programme
#   si le répertoire courant contient cette commande, on saisit:
#       ...$ ./demo...
#   si cette ligne était absente, il faudrait écrire
#       ...$ python <chemin_fichier>

import sys # librairie standard de python, voir https://docs.python.org/fr/3/library/sys.html
           # permet d'accéder à l'entrée et la sortie standard via sys.stdin et sys.stdout


lu = "peu importe!"
# ce programme ressemble à la commande echo
# il lit une ligne sur son entrée standard (le clavier)
# puis affiche cette même ligne sur sa sortie standard (l'écran)
# puis recommence. Pour le terminer, saisir <CTRL-D> (fin de fichier)
# on peut rediriger son entrée (<) ou sa sortie (>) (...voir cours)
while len(lu) > 0:
    lu = sys.stdin.readline()
    sys.stdout.write(lu.upper())
