import Traitement_Image as TI


class Affichage:

    def __init__(self):
        pass

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
            TI.print_card("./illustration/Sorciére.jpg", 50, 50)
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

    def cupidon(self, temp : bool, nom : str, nom : str):
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
        Return : NOne
        """
        TI.print_card("./illustration/faucheuse.jpg", 40, 40)
        pass



    """
    Méthode qui permettra un affichage d
    Parameters :
    Return :
    """
