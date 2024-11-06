from random import randint
from Joueur import Joueur

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
        nom = input("Nom de la partie : ")
        while nom == "":
            nom = input("Nom de la partie : ")
        self.id_partie = nom

        nb =  input("Nombre de joueurs [6-18] : ")
        while int(nb) < 6 or int(nb) > 18:
            nb =  input("Nombre de joueurs [6-18] : ")

        self.nombre_joueur = int(nb)
        i = 0
        roles = self.get_roles()
        while i < self.nombre_joueur:
            tmp = input(f"Nom du joueur [{i+1}] :")
            if tmp != "":
                rand_role = roles.pop(randint(0,len(roles)-1))
                j = Joueur(tmp,rand_role)
                self.joueurs.append(j)
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
        for k in range(50): # rest screen
            print("\n")
        for role in self.get_roles():
            for i in range(0,self.nombre_joueur):
                joueur = self.joueurs[i]

                print(f"Passé l'appareil au Joueur {i+1} : {joueur.get_username()}")
                input("Presser entré :")
                role_joueur = joueur.get_role()
                if  role_joueur == role:
                    pass

                    for k in range(50):
                        print("\n")
                else:
                    for k in range(50):
                        print("\n")
                    print(f"Joueur {i+1} : {joueur.get_username()} \n ne n'est pas a vous de jouer...")
                    input("Presser entré :")


    def get_id(self):
        return self.id_partie

    def get_nombre_joueur(self):
        return self.nombre_joueur

    def get_etat(self):
        return self.etat_partie

if __name__ == "__main__":
    newparti = Partie()
    newparti.creer()
    newparti.tour()
