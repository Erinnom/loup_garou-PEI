from random import randint
from Affichage import Affichage
from Joueur import Joueur
from Role import Role
import json
import os


class Partie:
    def __init__(self):
        self.id_partie = ""
        self.nombre_joueur = 0
        self.joueurs = []
        self.etat_partie = 0
        self.action = Role()
        self.premier_tour = True
        self.afg = Affichage()
        self.joueur_en_jeux = 0
        self.role_en_jeux = 0

    def get_roles(self):
        """
        Objectif : Obtenir la liste des de la partie en fonction du nombre de joueur
        Entrée : Aucune
        Sortie : liste des roles
        """
        role_partie = [
            ['Loup Garous', 'Loup Garous', 'Voyante', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Loup Garous', 'Loup Garous', 'Voyante', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois'],
            ['Loup Garous', 'Loup Garous', 'Voyante', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois'],
            ['Cupidon', 'Loup Garous', 'Loup Garous', 'Voyante', 'Chasseur', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois'],
            ['Cupidon', 'Loup Garous', 'Loup Garous', 'Petite Fille', 'Voyante', 'Chasseur', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Cupidon', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante', 'Chasseur',
             'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante', 'Chasseur',
             'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Voleur', 'Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante',
             'Chasseur', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Voleur', 'Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante',
             'Chasseur', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois'],
            ['Voleur', 'Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante',
             'Chasseur', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois'],
            ['Voleur', 'Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante',
             'Chasseur', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Voleur', 'Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante',
             'Chasseur', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois'],
            ['Voleur', 'Cupidon', 'Loup Garous', 'Loup Garous', 'Loup Garous', 'Sorcière', 'Petite Fille', 'Voyante',
             'Chasseur', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois',
             'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois', 'Simple Villageois']
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

        nb = input("Nombre de joueurs [6-18] : ")
        while int(nb) < 6 or int(nb) > 18:
            nb = input("Nombre de joueurs [6-18] : ")

        self.nombre_joueur = int(nb)
        i = 0
        roles = self.get_roles()
        while i < self.nombre_joueur:
            tmp = input(f"Nom du joueur [{i + 1}] :")
            if tmp != "":
                rand_role = roles.pop(randint(0, len(roles) - 1))
                j = Joueur(tmp, rand_role)
                self.joueurs.append(j)
                i += 1
        self.afg.reinitialiser_screen()

    def sauvegarder(self):
        """
        Objectif : Méthode permettant de sauvegarder la partie en cours dans un document Json
        Entrée : Aucune
        Sortie : un fichier Json de sauvegarde
        """
        data = {"id_partie": self.id_partie,
                "nombre_joueur": self.nombre_joueur,
                "etat_partie": self.etat_partie,
                "joueurs": [x.get_data() for x in self.joueurs],
                "action": self.action.get_data(),
                "joueur_en_jeu" : self.joueur_en_jeux,
                "role_en_jeux": self.role_en_jeux
                }

        sauvegarde = json.dumps(data, indent=4)

        with open(self.id_partie + ".json", "w") as outfile:
            outfile.write(sauvegarde)

    def charger(self, id_partie: str):
        """
        Objectif : Méthode permettant de charger un fichier Json pour reprendre la partie là où elle s'est arrêté
        Entrée : id_partie : str
        Sortie : Aucune
        """
        while True:
            fichier = id_partie + ".json"
            if os.path.exists(fichier):
                with open(fichier) as file:
                    data = json.load(file)

                self.id_partie = data["id_partie"]
                self.nombre_joueur = data["nombre_joueur"]
                self.etat_partie = data["etat_partie"]
                self.joueur_en_jeux = data["joueur_en_jeux"]
                self.role_en_jeux = data["role_en_jeux"]
                self.action.load_data(data["action"])

                #Génère des joueurs et leurs donnes les bons attributs.
                for i in range(len(data["joueurs"])):
                    self.joueurs.append(Joueur(data["joueurs"][i]["prenom"], data["joueurs"][i]["role"]))
                    self.joueurs[i].est_maire = data["joueurs"][i]["maire"]
                    self.joueurs[i].votes = data["joueurs"][i]["votes"]
                    self.joueurs[i].est_mort = data["joueurs"][i]["mort"]
                    self.joueurs[i].marie = data["joueurs"][i]["marie"]

                return

            else:
                id_partie = input("Fichier inexistant resaisissez le nom :")

    def get_joueur_en_vie(self):
        """
        Objectif : Retourner une liste d'id des joueurs encore en jeux
        Entrée : aucune
        Sortie : liste d'entier entre 0 et nombre de joueurs
        """
        alv_joueurs_id = []  # liste des indices des joueurs encore en vie
        for i in range(0, self.nombre_joueur):
            if not self.joueurs[i].get_mort():
                alv_joueurs_id.append(i)
        return alv_joueurs_id

    def tour_nuit(self):
        """
        Objectif : faire un tour durant la nuit
        Entrée : Aucune
        Sortie : Aucune
        """
        self.etat_partie = 0
        self.afg.reinitialiser_screen()

        self.action.demasquage_petite_fille(self.joueurs)
        print("La nuit tombe sur le village de tierce lieux... Le Village s'endort...\n"
              "Les villageois dorment tous sur leurs deux oreilles... enfin presque...")

        # Obtention des joueurs encore en vie
        alv_joueurs_id = self.get_joueur_en_vie()  # Liste des indices des joueurs encore en vie

        # Liste des rôles
        roles = self.get_roles()
        while self.role_en_jeux < len(roles):  # Boucle sur les rôles
            while self.joueur_en_jeux < self.nombre_joueur:  # Boucle sur les joueurs
                joueur = self.joueurs[self.joueur_en_jeux]
                self.afg.reinitialiser_screen()
                self.afg.anonyme_screen()
                print(f"Passez l'appareil au Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()}")

                if input("Tapez [save] pour sauvegarder ou appuyez sur une autre touche pour continuer : ") == "save":
                    self.sauvegarder()
                    return 3

                # Exécution des actions si le joueur a le rôle correspondant
                role_joueur = joueur.get_role()
                role = roles[self.role_en_jeux]  # Récupérer le rôle actuel
                if role_joueur == role and self.joueur_en_jeux in alv_joueurs_id:
                        self.executer_action(role, joueur)
                        self.role_en_jeux += 1
                else:
                    print(f"Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()} \nCe n'est pas à vous de jouer...")
                    input("Appuyez sur Entrée pour continuer.")
                self.joueur_en_jeux +=1 # Passer au joueur suivant
            self.joueur_en_jeux = 0  # Réinitialisation des variables pour le prochain tour
        # Réinitialisation des variables pour le prochain tour
        self.etat_partie = 1
        self.role_en_jeux = 0
        self.joueur_en_jeux = 0
        print("La nuit est terminée, le village se réveille...")

    def executer_action(self, role, joueur):
        """Exécute l'action en fonction du rôle."""
        if role == "Loup Garous":
            self.action.loup_garou(self.joueurs, joueur)
        elif role == "Voyante":
            self.action.voyante(self.joueurs)
        elif role == "Simple Villageois":
            self.action.villageois(self.joueurs, joueur)
        elif role == "Sorcière":
            self.action.sorciere(self.joueurs)
        elif role == "Petite Fille":
            self.action.petite_fille(self.joueurs)
        elif role == "Chasseur":
            self.action.chasseur(self.joueurs)
        elif role == "Cupidon":
            self.action.cupidon(self.joueurs)
        elif role == "Voleur" and self.premier_tour:
            self.action.voleur(self.joueurs, joueur)
        else:
            print(f"Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()} \n ne n'est pas a vous de jouer...")
            input("Presser entré :")


    def tour_jour(self):
        """
        Objectif : faire un tour durant le jour
        Entrée : Aucune
        Sortie : Aucune
        """
        self.etat_partie = 1
        self.afg.reinitialiser_screen()

        #Test des conditions pour une fin de partie
        if self.fin_de_partie() in [0, 1, 2]:
            return self.fin_de_partie()

        # Actualisation des joueur encore en vie
        alv_joueurs_id = self.get_joueur_en_vie()  # liste des indices des joueurs encore en vie

        # Vote du village
        votes = [0] * self.nombre_joueur  # inialise la liste des votes
        while self.joueur_en_jeux < self.nombre_joueur:
        #for self.joueur_en_jeux in range(0, self.nombre_joueur):
            joueur = self.joueurs[self.joueur_en_jeux]
            print(f"Passez l'appareil au Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()}")

            if input("Tapez [save] pour sauvegarder ou appuyer sur n'importe quel touche pour continuer : ") == "save":
                self.sauvegarder()
                return 3

            if self.joueur_en_jeux not in alv_joueurs_id:
                print("Ohhh.. NON!! il semblerait que vous êtes mort...")

            else:
                print("Pour qui souhaitez vous voter :")
                print([str(i) + " : " + self.joueurs[i].get_prenom() for i in alv_joueurs_id], [])
                vote = int(input("Indice du joueur [1-" + str(self.nombre_joueur) + "] : "))
                while vote not in alv_joueurs_id:
                    vote = int(input("Indice du joueur [1-" + str(self.nombre_joueur) + "] : "))
                self.joueurs[vote].vote()
                votes[vote] += 1
                if joueur.get_maire():
                    self.joueurs[vote].vote()
                    votes[vote] += 1
            mort_indice = votes.index(max(votes))
            mort = self.joueurs[mort_indice]
            mort.set_mort(True)

            self.afg.afficher_texte(
                f"Le Joueur {mort_indice} plus connu sous le nom de {mort.get_prenom()} a ete pendu par le village... Il etait ... {mort.get_role()}")

            if (mort.get_role() == "Chasseur"):
                self.action.chasseur(self.joueurs)
            if (mort.est_maire()):
                self.action.nouveau_maire(self.joueurs, joueur)
                self.premier_tour = False

            # reset vote
            for i in alv_joueurs_id:
                self.joueurs[i].reset_vote()
            self.joueur_en_jeux+=1
        self.joueur_en_jeux = 0
        # Test des conditions pour une fin de partie
        if self.fin_de_partie() in [0, 1, 2]:
            return self.fin_de_partie()

        self.etat_partie = 0

    def tour(self):
        """
        Objectif : Méthode qui effectue tout un tour de jeu
        Entrée : Aucune
        Sortie : Aucune
        """

        if self.etat_partie == 0:
            # Tour de nuit
            result_nuit = self.tour_nuit()
            if result_nuit in [0, 1, 2, 3]:
                return result_nuit  # Fin de partie détectée pendant la nuit
        # Élection du premier maire
        if self.premier_tour:
            self.action.capitaine(self.joueurs)
        elif self.etat_partie == 1:
            # Tour de jour
            result_jour = self.tour_jour()
            if result_jour in [0, 1, 2, 3]:
                return result_jour  # Fin de partie détectée pendant le jour

        else:
            raise ValueError("Etat de partie non conforme")

    def fin_de_partie(self):
        """
        Objectif : Méthode qui permet de tester si la partie est finis ou non
        Entrée : Aucune
        Sortie : 0 si les loups gagnent, 1 si les villageois gagnent, 2 si les mariées gagnent
        """
        nb_loup = sum(1 for i in self.joueurs if i.get_role() == "Loup Garous")
        nb_joueurs = len(self.joueurs)

        #Victoire des mariées
        if nb_joueurs == 2 and self.joueurs[0].get_marie and self.joueurs[1].get_marie:
            return 2

        #Victoire des Villageois
        elif nb_loup == 0 and nb_joueurs != 0:
            return 1

        #Victoire des loups
        elif nb_loup >= nb_joueurs - nb_loup:
            return 0

    def get_id(self):
        """
        Objectif : Obtenir l'id de la partie
        Entrée : Aucune
        Sortie : id de la partie
        """
        return self.id_partie

    def get_nombre_joueur(self):
        """
        Objectif : Obtenir le nombre de joueur de la partie
        Entrée : Aucune
        Sortie : nombre de joueur
        """
        return self.nombre_joueur

    def get_etat(self):
        """
        Objectif : Obtenir l'état de la partie
        Entrée : Aucune
        Sortie : état de la partie
        """
        return self.etat_partie

    def __str__(self):
        """
        Objectif : Renvoie le statut de la partie formaté correctement
        Entrée : Aucune
        Sortie : string
        """
        res = ""
        res += "Id Partie : " + str(self.id_partie) + "\n"
        res += "Etat Partie : " + str(self.etat_partie) + "\n"
        res += "Nombre de joueurs : " + str(self.nombre_joueur) + "\n"
        for joueur in self.joueurs:
            res += str(joueur) + "\n"
        return res


if __name__ == "__main__":
    test = Partie()
    test.creer()
    test.tour_jour()
