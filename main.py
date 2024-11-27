"""
main.py

script principal du projet loup garou PEI

Auteurs :
- Fauviau Elliot (@elliot.fauviau)
- Laudy Merlin   (@laudymerlin1 / @ThecraftM)
- Monnier Maxime (@Erinnom)
- Ramos Axel     (@Ulyclash)
"""
#Import
from Partie import *
from Affichage import Affichage


# Déclatation de Variables
partie_actuelle = Partie()
screen_display = Affichage()


# Programme Principal
"""
Programme principal qui fait se dérouler la partie correctement
"""

screen_display.menu_principal()
choix = int(input())
while choix not in [1,2,3]:
    choix = int(input())

#choix n°1 création d'une nouvelle partie
if choix == 1:
    partie_actuelle.creer()

#choix n°2 charge une partie grâce à son nom de fichier (extension non nécessaire)
if choix == 2:
    screen_display.selection_fichier()
    partie_actuelle.charger(input())

#choix n°3 permet la sortie du programme
if choix == 3:
    raise SystemExit(0)
"""
while partie_actuelle.tour() == 0:
    partie_actuelle.tour()

if partie_actuelle.tour() == 1:
    pass"""