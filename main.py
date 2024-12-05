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

# Déclaration de Variables
partie_actuelle = Partie()
screen_display = Affichage()

# Programme Principal
"""
Programme principal qui fait se dérouler la partie correctement
"""

screen_display.menu_principal()
choix = int(input("Votre choix : "))
while choix not in [1, 2, 3]:
    choix = int(input("Votre choix : "))

#choix n°1 création d'une nouvelle partie
if choix == 1:
    partie_actuelle.creer()

#choix n°2 charge une partie grâce à son nom de fichier (extension non nécessaire)
if choix == 2:
    partie_actuelle.charger(input("Entrez le nom de votre sauvegarde : "))

#choix n°3 permet la sortie du programme
if choix == 3:
    raise SystemExit(0)

active = True
while active:
    status = partie_actuelle.tour()
    if status == 3:
        active = False

    elif status == 2:
        screen_display.afficher_texte("Les mariés ont gagnés !")
        active = False

    elif status == 1:
        screen_display.afficher_texte("Les villageois ont gagnés !")
        active = False

    elif status == 0:
        screen_display.afficher_texte("Les loups-garous ont gagnés !")
        active = False

raise SystemExit(0)