# Import de la librairie random
from random import randint

class Joueur:
    """
    Class : Joueur
    Attributs : prenom (str), role (str), est_maire (bool)
    Méthodes : set_role(self,role:str), set_maire(self,est_maire:bool = 0),get_maire(self),get_role(self),get_prenom(self)
    """
    # Attributs
    prenom = "" # prenom du joueur
    role = "" # role du joueur
    est_maire = 0 # booleen 1 si maire 0 sinon

    # Constructeur
    def _init_ (self, prenom = "Joueur" + str(randint(0,1000)),role = "villageois"): # Nom par défaut dans le cas ou le prenom est vide
        self.prenom = str(prenom)

    # Méthodes

    def set_role(self,role:str):
        """
        Objectif : Définir l'attribut role au role choisit
        Entrée : Nom du role
        Sortie : Aucune
        """
        self.role = str(role)


    def set_maire(self,est_maire:bool = 0):
        """
        Objectif : Définir le joueur comme maire
        Entrée : booleen 1 si maire 0 sinon
        Sortie : Aucune
        """
        self.est_maire = int(est_maire)


    def get_maire(self):
        """
        Objectif : Renvoyer le booleen 1 si maire 0 sinon
        Entrée : Aucune
        Sortie : booleen 1 si maire 0 sinon
        """
        return self.est_maire


    def get_role(self):
        """
        Objectif : Renvoyer le role du joueur
        Entrée : Aucune
        Sortie : le role du joueur
        """
        return self.role


    def get_prenom(self):
        """
        Objectif : Renvoyer le nom du joueur
        Entrée : Aucune
        Sortie : nom du joueur
        """
        return self.prenom
