from _typeshed import Self
from random import randint
import Joueur

class Partie():
    def __init__(self):
        self.id_partie = ""
        self.nombre_joueur = 0
        self.joueurs = []
        self.etat_partie = 0

    def get_roles(self):
        """
        Objectif : Obtenir la liste des de la partie en fonction du nombre de joueur
        Entrée : Aucune
        Sortie : liste des roles
        """
        role_partie = [
            ["Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Capitaine"],  # 6 joueurs
            ["Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Capitaine"],  # 7 joueurs
            ["Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Capitaine"],  # 8 joueurs
            ["Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Chasseur", "Cupidon"],  # 9 joueurs
            ["Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Petite Fille", "Chasseur", "Cupidon"],  # 10 joueurs
            ["Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Sorcière", "Chasseur", "Cupidon"],  # 11 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Petite Fille", "Chasseur", "Cupidon", "Voleur"],  # 12 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Sorcière", "Chasseur", "Cupidon", "Voleur"],  # 13 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Petite Fille", "Chasseur", "Cupidon", "Voleur"],  # 14 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Sorcière", "Chasseur", "Cupidon", "Voleur"],  # 15 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Sorcière", "Petite Fille", "Chasseur", "Cupidon", "Voleur"],  # 16 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Sorcière", "Petite Fille", "Chasseur", "Cupidon", "Voleur"],  # 17 joueurs
            ["Loup Garou", "Loup Garou", "Loup Garou", "Loup Garou", "Voyante", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Simple Villageois", "Sorcière", "Petite Fille", "Chasseur", "Cupidon", "Voleur"]  # 18 joueurs
        ]
        return role_partie[self.nombre_joueur - 6]

    def get_joueurs(self):
        """
        Objectif : Obtenir la liste des joueurs de la partie
        Entrée : Aucune
        Sortie : liste des joueurs
        """
        return self.joueurs

    def creer(self):
        """
        Objectif : Creer une nouvelle partie
        Entrée : Aucune
        Sortie : Aucune
        """
        tmp = input("Nom de la partie : ")
        while tmp == "":
            tmp = input("Nom de la partie : ")
        self.id_partie = tmp

        tmp =  input("Nombre de joueurs [6-18] : ")
        while int(tmp) < 6 or int(tmp) > 18:
            tmp =  input("Nombre de joueurs [6-18] : ")

        self.nombre_joueur = int(tmp)
        i = 0
        roles = self.get_roles()
        while i < self.nombre_joueur:
            tmp = input(f"Nom du joueur [{i+1}] :")
            if tmp != "":
                self.joueurs.append(Joueur(tmp,roles.pop(randint(0,self.nombre_joueur -i-1))))
                i+=1

    def sauvegarder(self, nom_fichier: str):
        """Méthode permettant de sauvegarder la partie en cours
            dans un document Json"""
        pass

    def charger(self, id_partie: str):
        """Méthode permettant de charger un fichier Json pour
            reprendre la partie là où elle c'est arrêté"""
        pass

    def tour(self):
        """Méthode qui effectue tout un tour de jeu"""
        pass

    def get_id(self):
        return self.id_partie

    def get_nombre_joueur(self):
        return self.nombre_joueur

    def get_etat(self):
        return self.etat_partie



if __name__ == "__main__":
    pass
