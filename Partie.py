from random import randint
from typing_extensions import _F
from Affichage import *
from Joueur import Joueur
from Role import Role
import json

class Partie():
    def __init__(self):
        self.id_partie = ""
        self.nombre_joueur = 0
        self.joueurs = []
        self.etat_partie = 0
        self.action = Role()
        self.premier_tour = True

    def get_roles(self):
        """
        Objectif : Obtenir la liste des de la partie en fonction du nombre de joueur
        Entrée : Aucune
        Sortie : liste des roles
        """
        role_partie = [
            ['Loup Garous','Loup Garous','Voyante','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Loup Garous','Loup Garous','Voyante','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Loup Garous','Loup Garous','Voyante','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Cupidon','Loup Garous','Loup Garous','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Cupidon','Loup Garous','Loup Garous','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Cupidon','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Voleur','Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Voleur','Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Voleur','Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Voleur','Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Voleur','Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois'],
            ['Voleur','Cupidon','Loup Garous','Loup Garous','Loup Garous','Sorcière','Petite Fille','Voyante','Chasseur','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois','Simple Villageois']
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
                "joueurs" : [x.get_data() for x in self.joueurs],
                "action" : self.action.get_data()
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
        self.action.load_data(data["action"])

        #Génère des joueurs et leurs donnes les bons attributs.
        for i in range(len(data["joueurs"])):
            self.joueurs.append(Joueur(data["joueurs"][i]["prenom"], data["joueurs"][i]["role"]))
            self.joueurs[i].est_maire = data["joueurs"][i]["maire"]
            self.joueurs[i].votes = data["joueurs"][i]["votes"]
            self.joueurs[i].est_mort = data["joueurs"][i]["mort"]
            self.joueurs[i].marie = data["joueurs"][i]["marie"]

    def tour(self):
        """Méthode qui effectue tout un tour de jeu"""
        afg = Affichage()
        self.action.demasquage_petite_fille(self.joueurs)
        print("La nuit tombe sur le village de tierce lieux... Le Village s'endort...\n les villageois dorment tous sur leurs deux oreilles... enfin presque...")

        # Obtention des joueurs encore en liste
        alv_joueurs_id = [] # liste des indices des joueurs encore en vie
        for i in range(0,self.nombre_joueur):
            if not self.joueurs[i].get_mort():
                alv_joueurs_id.append(i)

        # Boucle pour faire jouer tous les rôles
        for role in self.get_roles():

            # Boucle afin de faire jouer les rôles en fonctiton de son rôle
            for i in range(0,self.nombre_joueur):
                joueur = self.joueurs[i]
                print(f"Passé l'appareil au Joueur {i+1} : {joueur.get_prenom()}")
                input("Presser entré :")

                role_joueur = joueur.get_role()
                if  role_joueur == role and i in alv_joueurs_id:
                    if role == "Loup Garou":
                        self.action.loup_garou(self.joueurs,joueur)
                    elif role == "Voyante":
                        self.action.voyante(self.joueurs)
                    elif role == "Simple Villageois":
                        self.action.villageois(joueur)
                    elif role == "Sorcière":
                        self.action.sorciere(self.joueurs)
                    elif role == "Petite Fille":
                        self.action.petite_fille(self.joueurs)
                    elif role == "Chasseur":
                        self.action.chasseur(self.joueurs)
                    elif role == "Cupidon":
                        self.action.cupidon(self.joueurs)
                    elif role == "Voleur" and self.premier_tour:
                        self.action.voleur(self.joueurs)
                    else:
                        print(f"Joueur {i+1} : {joueur.get_username()} \n ne n'est pas a vous de jouer...")
                        input("Presser entré :")
                else:
                    print(f"Joueur {i+1} : {joueur.get_username()} \n ne n'est pas a vous de jouer...")
                    input("Presser entré :")

        # Actualisation des joueur encore en vie
        alv_joueurs_id = [] # liste des indices des joueurs encore en vie
        for i in range(0,self.nombre_joueur):
            if not self.joueurs[i].get_mort():
                alv_joueurs_id.append(i)

        # Election du premier maire
        if self.premier_tour:
            self.action.capitaine(self.joueurs)

        # Vote du village
        votes = [0] * self.nombre_joueur # inialise la liste des votes
        for i in range(0,self.nombre_joueur):
            joueur = self.joueurs[i]
            print(f"Passé l'appareil au Joueur {i+1} : {joueur.get_username()}")
            input("Presser entré :")
            if i not in alv_joueurs_id:
                print("Ohhh.. NON!! il semblerait que vous êtes mort...")
            else:
                print("Pour qui souhaitez vous voter :")
                afg.liste_joueurs([str(i) + " : " + self.joueurs[i].get_prenom() for i in alv_joueurs_id],[])
                vote = int(input("Indice du joueur [1-"+str(self.nombre_joueur)+"] : "))
                while vote not in alv_joueurs_id:
                    vote = int(input("Indice du joueur [1-"+str(self.nombre_joueur)+"] : "))
                self.joueurs[vote].vote()
                votes[vote]+=1
                if joueur.get_maire():
                    self.joueurs[vote].vote()
                    votes[vote]+=1
            mort_indice = votes.index(max(votes))
            mort = self.joueurs[mort_indice]
            mort.set_mort(True)
            print(f"Le Joueur {mort_indice} plus connu sous le nom de {mort.get_prenom()} à été pendu par le village... Il était ... {mort.get_role()}")
            if (mort.get_role() == "Chasseur"):
                 self.action.chasseur(self.joueurs)
            if (mort.est_maire()):
                 self.action.nouveau_maire(self.joueurs)
        self.premier_tour = False



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
