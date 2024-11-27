import Traitement_Image as TI
import os as os
from pyfiglet import Figlet




class Affichage:

    def __init__(self):
        pass


    """#####################################################################################################################################################

                                                                        AFFICHAGE IMAGES

    #####################################################################################################################################################"""
    def jour(self):
        """
        Méthode qui permettra un affichage d'un fond illustrant la journee et l'arrivee du vote
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/jour.jpg", 70, 60)
        pass

    def nuit(self):
        """
        Méthode qui permettra un affichage d'un fond illustrant la nuit et l'arrivee des differents rôles
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/nuit.jpg", 70, 60)
        pass

    def loup_garou(self, temp : bool, nom : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """
        if temp :
            TI.print_card("./illustration/LG.jpg", 50, 50)
        else :
            TI.print_card("./illustration/griffes.jpg", 40, 40)
        pass

    def sorciere(self, temp : bool, choix : bool, nom : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """
        if temp :
            TI.print_card("./illustration/Sorciere.jpg", 50, 50)
        else :
            TI.print_card("./illustration/potion.jpg", 40, 40)
        pass


    def chasseur(self, temp : bool, nom : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """
        if temp :
            TI.print_card("./illustration/Chasseur.jpg", 50, 50)
        else :
            TI.print_card("./illustration/cible.jpg", 40, 40)
        pass

    def petite_fille(self, temp : bool):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage
        Return : None
        """
        if temp :
            TI.print_card("./illustration/Petite-Fille.jpg", 50, 50)
        else :
            TI.print_card("./illustration/ours.jpg", 40, 40)
        pass

    def voleur(self, temp : bool, nom : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """
        if temp :
            TI.print_card("./illustration/Voleur.jpg", 50, 50)
        else :
            TI.print_card("./illustration/pas.jpg", 40, 40)
        pass

    def cupidon(self, temp : bool, nom1 : str, nom2 : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom des joueurs vises
        Return : None
        """
        if temp :
            TI.print_card("./illustration/Cupidon.jpg", 50, 50)
        else :
            TI.print_card("./illustration/coeur.jpg", 50, 40)
        pass

    def voyante(self, temp : bool, nom : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """
        if temp :
            TI.print_card("./illustration/Voyante.jpg", 50, 50)
        else :
            TI.print_card("./illustration/boule.jpg", 40, 40)
        pass

    def villageois(self):
        """
        Méthode qui permettra un affichage de l'affichage de la carte
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/Villageois.jpg", 50, 50)
        pass

    def capitaine(self, nom : str):
        """
        Méthode qui permettra un affichage de l'affichage de la carte
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/Capitaine.jpg", 50, 50)
        pass

    def voter(self, nom : str):
        """
        Méthode qui permettra un affichage de la seance de vote
        Parameters : None
        Return :
        """
        TI.print_card("./illustration/lettre.jpg", 40, 40)
        pass

    def votes(self, joueurs):
        """
        Méthode qui permettra un affichage les votes pour chacun des joueurs
        Parameters : la liste des objets de type joueur
        Return : None
        """
        TI.print_card("./illustration/lettre-ouverte.jpg", 40, 40)
        pass

    def eliminer(self, nom : str):
        """
        Méthode qui permettra un affichage du joueur qui a été éliminé
        Parameters : nom du joueur
        Return : None
        """
        TI.print_card("./illustration/faucheuse.jpg", 40, 40)
        pass

    def anonyme_screen(self):
        """
        Méthode qui permettra un affichage de l'écran d'attente, pour tous les joueurs à qui ce ne sera pas le tour de jouer
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/bandeau.jpg", 50, 30)
        pass

    def reinitialiser_screen(self):
        """
        Méthode qui permettra d'effacer le terminal
        Parameters : None
        Return : None
        """
        os.system("clear")
        pass

    """#####################################################################################################################################################

                                                                AFFICHAGE TEXTE

    #####################################################################################################################################################"""


    """
    Méthode qui permettra d'afficher la liste des joueurs
    Parameters : Liste des joueurs, lliste des alliés
    Return : None
    """
    def liste_joueurs(self,  l : list, allies : list):
        #Caractères pour construire le tableau
        char = ["┌", "┐", "└", "┘", "┴", "┬","─", "├", "┼", "┤", "│"]

        #Couleurs pour différencier allies et ennemis
        RED = "\033[31m"
        GREEN = "\033[32m"
        BLUE = "\033[34m"
        RESET = "\033[0m"

        length = len(l)
        max = 0

        for j in l:
            if len(j) > max:
                max = len(j)

        """
        Fonction qui affiche le contours du tableau (ligne du haut)
        Parameters : None
        Return : None
        """
        def ligne_haut(t):
            print(char[0], end = "")
            for _ in range(t):
                for __ in range (max+4):
                    print(char[6], end ="")
                if _ != t-1:
                    print(char[5], end = "")
            print(char[1])
            return

        """
        Fonction qui affiche le contours du tableau (ligne du bas)
        Parameters : None
        Return : None
        """
        def ligne_bas(t):
            print()
            print(char[2], end="")
            for _ in range(t):
                for __ in range (max+4):
                    print(char[6], end ="")
                if _ != t-1:
                    print(char[4], end = "")
            print(char[3])
            return

        ligne_supp = 0
        if len(l) < 10:
            t = len(l)
        else :
            t = 10
        if length%10 != 0:
            ligne_supp +=1

        #Affichage des prénoms dans le tableau

        for joueur in range (length//10 + ligne_supp):
            ligne_haut(t)
            print(char[-1], end = "")
            for _ in range(10):
                if l == [] :
                    for __ in range (max+4):
                        print(" ", end ="")
                else :
                    nom = l.pop(0)
                    ecart = max-len(nom)
                    for __ in range (ecart//2+2):
                        print(" ", end = "")
                    if nom in allies:
                        print(f"{RED}{nom}{RESET}", end="")

                    else :
                        print(f"{GREEN}{nom}{RESET}", end="")
                    for __ in range (ecart//2 + ecart%2 +2):
                        print(" ", end = "")
                    print(char[-1], end ="")

            ligne_bas(t)

        return


    """
    Méthode qui permettra d'afficher du etxte, avec de la couleur sur une partie si voulu
    Parameters : texte, texte à colorer, couleur
    Return : None
    """
    def phrases(self, text : str, text_color : str,  color = "WHITE"):
        COLORS = {
            "BLACK": "\033[30m",
            "RED": "\033[31m",
            "GREEN": "\033[32m",
            "YELLOW": "\033[33m",
            "BLUE": "\033[34m",
            "MAGENTA": "\033[35m",
            "CYAN": "\033[36m",
            "PINK": "\033[38;5;205m",
            "WHITE": "\033[37m",
        }
        RESET = "\033[0m"
        DEFAUT = "WHITE"
        color = color.upper()
        if color not in COLORS:
            color = "WHITE"
        if text_color != "" :
            avant, milieu, apres = text.partition(text_color)
            print(f"{COLORS[DEFAUT]}{avant}{RESET}", end ="")
            print(f"{COLORS[color]}{milieu}{RESET}", end ="")
            print(f"{COLORS[DEFAUT]}{apres}{RESET}")
        else :
            print(f"{COLORS[DEFAUT]}{text}{RESET}")
        return
<<<<<<< HEAD
=======

    """
    Méthode qui permettra d'afficher le menu d'acceuil du jeu
    Parameters : None
    Return : None
    """
    def menu_principal(self):
        self.afficher_texte('Loup - Garou', 'big')
        print(f"\n \t\t\t\t\t🄼 🄰 🄳 🄴  🄱 🅈  🄼 🄴 🄰 🄼  🅃 🄴 🄰 🄼\n")
        options = [
            "ℂ𝕣𝕖́𝕖𝕣 𝕦𝕟𝕖 𝕡𝕒𝕣𝕥𝕚𝕖 - 𝟙",
            "ℂ𝕙𝕒𝕣𝕘𝕖𝕣 𝕦𝕟𝕖 𝕡𝕒𝕣𝕥𝕚𝕖 - 𝟚",
            "ℚ𝕦𝕚𝕥𝕥𝕖𝕣 𝕝𝕖 𝕛𝕖𝕦 - 𝟛"

        ]
        for o in options:
            print()
            print("\t\t\t\t\t", o)

        print("\n\n")
        return

    """
    Méthode qui permettra d'afficher le menu de chargement d'une partie
    Parameters : None
    Return : None
    """
    def menu_partie(self):
        pass
        return


    def afficher_texte(self, texte : str, font_t = 'big'):
        f = Figlet(font=font_t)
        print(f.renderText(texte))
>>>>>>> Partie



objet = Affichage()
<<<<<<< HEAD
=======
objet.menu_principal()
objet.menu_partie()
>>>>>>> Partie
