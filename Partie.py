from random import randint
from Joueur import *
from Role import *
import json

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

    def sauvegarder(self):
        """Méthode permettant de sauvegarder la partie en cours
            dans un document Json"""
        data = {"id_partie" : self.id_partie,
                "nombre_joueur" : self.nombre_joueur,
                "etat_partie" : self.etat_partie,
                "joueurs" : [x.get_data() for x in self.joueurs]
                }

        sauvegarde = json.dumps(data, indent=4)

        with open(self.id_partie + ".json", "w") as outfile:
            outfile.write(sauvegarde)

    def charger(self, id_partie: str):
        """Méthode permettant de charger un fichier Json pour
            reprendre la partie là où elle s'est arrêté"""
        with open(id_partie+".json") as file:
            data = json.load(file)

        self.id_partie = data["id_partie"]
        self.nombre_joueur = data["nombre_joueur"]
        self.etat_partie = data["etat_partie"]

        #Génère des joueurs et leurs donnes les bons attributs.
        for i in range(len(data["joueurs"])):
            self.joueurs.append(Joueur(data["joueurs"][i]["prenom"], data["joueurs"][i]["role"]))
            self.joueurs[i].est_maire = data["joueurs"][i]["maire"]
            self.joueurs[i].votes = data["joueurs"][i]["votes"]
            self.joueurs[i].est_mort = data["joueurs"][i]["mort"]
            self.joueurs[i].marie = data["joueurs"][i]["marie"]

    def tour(self):
        """Méthode qui effectue tout un tour de jeu"""
        rls = Role()
        rls.demasquage_petite_fille()
        print("La nuit tombe sur le village de tierce lieux... Le Village s'endore...\n les villageois dorment tous sur leurs deux oreilles... enfin presque...")
        for role in self.get_roles():
            for i in range(0,self.nombre_joueur):
                joueur = self.joueurs[i]
                rls = Role()
                print(f"Passé l'appareil au Joueur {i+1} : {joueur.get_username()}")
                input("Presser entré :")
                role_joueur = joueur.get_role()
                if  role_joueur == role:
                    if role == "Loup Garou":
                        rls.loup_garou()
                    elif role == "Voyante":
                        rls.voyante()
                    elif role == "Simple Villageois":
                        rls.villageois()
                    elif role == "Sorcière":
                        rls.sorciere()
                    elif role == "Petite Fille":
                        rls.petite_fille()
                    elif role == "Chasseur":
                        rls.chasseur()
                    elif role == "Cupidon":
                        rls.cupidon()
                    elif role == "Voleur":
                        rls.voleur()
                    else:
                        print("Erreur")
                #else:
                    #for k in range(50):
                    #    print("\n")
                    #print(f"Joueur {i+1} : {joueur.get_username()} \n ne n'est pas a vous de jouer...")
                    #input("Presser entré :")
        for i in range(0,self.nombre_joueur):



    def get_id(self):
        return self.id_partie

    def get_nombre_joueur(self):
        return self.nombre_joueur

    def get_etat(self):
        return self.etat_partie

    def __str__(self):
        """
        Renvoie le statut de la partie formaté correctement
        """
        res = ""
        res += "Id Partie : " + str(self.id_partie) + "\n"
        res += "Etat Partie : " + str(self.etat_partie) + "\n"
        res += "Nombre de joueurs : " + str(self.nombre_joueur) + "\n"
        for joueur in self.joueurs:
            res += str(joueur) + "\n"
        return res

if __name__ == "__main__":
    pass
