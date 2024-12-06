import time
from random import *
import random
from Affichage import Affichage
from Joueur import Joueur
from Role import Role
import json
import os
import string



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

    def get_indice_joueur(self,prenom:str)->int:
        i = 0
        while i < self.nombre_joueur and self.joueurs[i].get_prenom() != prenom:
            i+=1
        if i < self.nombre_joueur and self.joueurs[i].get_prenom() == prenom :
            return i
        return -1

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

        while True:
            try:
                nb = int(input("Nombre de joueurs [6-18] : "))
                if 6 <= nb <= 18:
                    break
                else:
                    print("Valeur non valide, entrez un nombre entre 6 et 18.")
            except ValueError:
                print("Saisie non valide, veuillez entrer un nombre.")

        self.nombre_joueur = int(nb)
        i = 0
        roles = self.get_roles()
        print()
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
                self.joueur_en_jeux = data["joueur_en_jeu"]
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
        self.afg.nuit()

        # Obtention des joueurs encore en vie
        alv_joueurs_id = self.get_joueur_en_vie()  # Liste des indices des joueurs encore en vie

        # Liste des rôles
        roles = self.get_roles()
        while self.role_en_jeux < len(roles):  # Boucle sur les rôles
            while self.joueur_en_jeux < self.nombre_joueur and self.role_en_jeux < len(roles):  # Boucle sur les joueurs
                joueur = self.joueurs[self.joueur_en_jeux]
                self.afg.reinitialiser_screen()
                self.afg.anonyme_screen()
                print()
                print()
                print(f"Passez l'appareil au Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()}")
                print()
                print()
                if input("Tapez [save] pour sauvegarder ou appuyez sur une autre touche pour continuer : ") == "save":
                    self.sauvegarder()
                    return 3

                # Exécution des actions si le joueur a le rôle correspondant
                role_joueur = joueur.get_role()
                role = roles[self.role_en_jeux]  # Récupérer le rôle actuel
                if role_joueur == role:
                    self.afg.reinitialiser_screen()
                    if  self.joueur_en_jeux in alv_joueurs_id:
                        self.afg.afficher_texte(joueur.get_prenom(), "blocky")
                        self.executer_action(role, joueur)
                    self.role_en_jeux += 1
                else:
                    self.afg.reinitialiser_screen()
                    self.afg.afficher_texte(joueur.get_prenom(), "blocky")
                    print("\n\nCe n'est pas à vous de jouer...")
                    self.demander_recopie()
                self.joueur_en_jeux +=1 # Passer au joueur suivant
            self.joueur_en_jeux = 0  # Réinitialisation des variables pour le prochain tour
        # Réinitialisation des variables pour le prochain tour
        self.etat_partie = 1
        self.role_en_jeux = 0
        self.joueur_en_jeux = 0

        self.afg.jour()


    def executer_action(self, role, joueur):
        """
        Exécute l'action en fonction du rôle.
        """

        if role == "Cupidon" and self.premier_tour:
            self.action.cupidon(self.joueurs)
        elif role == "Loup Garous":
            self.action.loup_garou(self.joueurs, joueur)
        elif role == "Voyante":
            self.action.voyante(self.joueurs)
        elif role == "Sorcière":
            self.action.sorciere(self.joueurs)
        elif role == "Petite Fille":
            self.action.petite_fille(self.joueurs)
        elif role == "Chasseur":
            self.action.chasseur(self.joueurs)
        elif role == "Voleur" and self.premier_tour:
            self.action.voleur(self.joueurs, joueur)
        else:
            print(f"Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()} \n ne n'est pas a vous de jouer...")
            self.demander_recopie()


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
        prenoms = [self.joueurs[i].get_prenom() for i in alv_joueurs_id]
        # Vote du village
        while self.joueur_en_jeux < self.nombre_joueur:
            self.afg.reinitialiser_screen()
            #for self.joueur_en_jeux in range(0, self.nombre_joueur):
            joueur = self.joueurs[self.joueur_en_jeux]
            print(f"Passez l'appareil au Joueur {self.joueur_en_jeux + 1} : {joueur.get_prenom()}")

            if input("Tapez [save] pour sauvegarder ou appuyer sur n'importe quel touche pour continuer : ") == "save":
                self.sauvegarder()
                return 3
            self.afg.afficher_texte(joueur.get_prenom(), "blocky")
            if self.joueur_en_jeux not in alv_joueurs_id:
                print("Ohhh.. NON!! il semblerait que vous soyez mort...")

            else:
                self.afg.liste_joueurs(prenoms, [])
                vote = input("Nom du joueur que vous voulez éliminer : ")
                while vote not in prenoms:
                    vote = input("Nom du joueur que vous voulez éliminer : ")
                indice_joueur = self.get_indice_joueur(vote)
                self.joueurs[indice_joueur].vote()
                #votes[indice_joueur] += 1
                if joueur.get_maire():
                    self.joueurs[indice_joueur].vote()
                    #votes[indice_joueur] += 1
            self.joueur_en_jeux += 1

        mort_indice = self.get_indice_mort()
        mort = self.joueurs[mort_indice]
        mort.set_mort(True)

        self.afg.afficher_texte(
                f"Le Joueur {mort_indice} plus connu sous le nom de {mort.get_prenom()} a ete pendu par le village... Il etait ... {mort.get_role()}")
        if (mort.get_role() == "Chasseur"):
                self.action.chasseur(self.joueurs)
        if (mort.get_maire() == 1):
            self.action.nouveau_maire(self.joueurs,mort)
            self.premier_tour = False

        # reset vote
        for i in self.joueurs:
            i.reset_vote()
        self.joueur_en_jeux+=1
        self.joueur_en_jeux = 0
        # Test des conditions pour une fin de partie
        if self.fin_de_partie() in [0, 1, 2]:
            return self.fin_de_partie()

        self.etat_partie = 0
        if input("Tapez [save] pour sauvegarder ou appuyer sur n'importe quel touche pour continuer : ") == "save":
            self.sauvegarder()
            return 3

    def get_indice_mort(self):
        votes = [0] * self.nombre_joueur  # inialise la liste des votes
        for i in range (self.nombre_joueur):
            votes[i] = self.joueurs[i].get_vote()

        max_vote = max(votes)
        indice_joueur_max_vote = []
        for i in range (self.nombre_joueur):
            if votes[i] ==  max_vote:
                indice_joueur_max_vote.append(i)

        return indice_joueur_max_vote[randint(0,len(indice_joueur_max_vote)-1)]

    def tour(self):
        """
        Objectif : Méthode qui effectue tout un tour de jeu
        Entrée : Aucune
        Sortie : Aucune
        """
        # Premier tour
        if self.premier_tour and self.etat_partie == 1:
            self.action.capitaine(self.joueurs)

        if self.etat_partie == 0:
            # Tour de nuit
            result_nuit = self.tour_nuit()
            if result_nuit in [0, 1, 2, 3]:
                return result_nuit  # Fin de partie détectée pendant la nuit

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


    def revelation_role(self):
        """
        Objectif : Reveal le rôle de chaque joueur au début du jeu
        Entrée : Aucune
        Sortie : Aucune
        """

        for i in self.joueurs:
            role = i.get_role()
            self.afg.afficher_texte(i.get_prenom())
            input("Appuyez sur entrer pour réveler votre role")
            self.afg.reinitialiser_screen()
            if role == "Cupidon":
                self.afg.print_cards("./illustration/Cupidon.jpg")
            elif role == "Loup Garous":
                self.afg.print_cards("./illustration/LG.jpg")
            elif role == "Voyante":
                self.afg.print_cards("./illustration/Voyante.jpg")
            elif role == "Simple Villageois":
                self.afg.print_cards("./illustration/Villageois.jpg")
            elif role == "Sorcière":
                self.afg.print_cards("./illustration/Sorciere.jpg")
            elif role == "Petite Fille":
                self.afg.print_cards("./illustration/Petite-Fille.jpg")
            elif role == "Chasseur":
                self.afg.print_cards("./illustration/Chasseur.jpg")
            elif role == "Voleur":
                self.afg.print_cards("./illustration/Voleur.jpg")

            print()
            input("Appuyer sur entrer puis passez l'appareil au joueur suivant ")
            self.afg.reinitialiser_screen()

    def generer_chaine_aleatoire(self,longueur):
        """Génère une chaîne aléatoire composée de lettres et chiffres."""
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choices(caracteres, k=longueur))

    def demander_recopie(self):
        """Demande à l'utilisateur de recopier une chaîne générée aléatoirement."""
        chaine_a_recopier = self.generer_chaine_aleatoire(10)  # Par défaut, 10 caractères
        while True:
            print(f"Recopiez exactement cette chaîne : '{chaine_a_recopier}'")
            saisie = input("> ")
            if saisie == chaine_a_recopier:
                return
            else:
                print("Erreur : Vous n'avez pas recopié la chaîne correctement. Essayez encore.")

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
