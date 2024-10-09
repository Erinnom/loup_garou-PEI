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
    votes = 0
    # Constructeur
    def __init__ (self, prenom, role): # Nom par défaut dans le cas ou le prenom est vide
        self.prenom = str(prenom)
        self.role = str(role)

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
        return str(self.role)


    def get_prenom(self):
        """
        Objectif : Renvoyer le nom du joueur
        Entrée : Aucune
        Sortie : nom du joueur
        """
        return self.prenom

    def vote(self):
        self.vote = self.vote+1

    def get_vote(self):
        return self.vote

    def reset_vote(self):
        self.vote = 0
# Test

j1 = Joueur("Maxime","sorcière")
print(f"{j1.get_prenom()} {j1.get_role()}")
