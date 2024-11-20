from random import *
import Affichage as affichage
import Joueur
import Partie
import random

class Role():
    def __init__(self):

        self.potion_vie = True
        self.potion_mort = True
        self.lettre_loup_garou = []
        self.lettre_petite_fille = []
        self.mort_tour = []
        self.mort =[]

        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        self.loup = [joueur.get_prenom() for joueur in liste if joueur.get_role() == "Loup Garou"]
        self.vote_loup = []

    """Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables
    paramètre : moment
    """
    def sorciere(self):

        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        prenom = []
        for i in range(0, len(liste)):
            prenom.append(liste[i].get_prenom())

        print("Liste des joueurs dans la partie : " + str(prenom))

        if self.potion_vie == True:
            print("Voulez vous utiliser votre potion de vie, oui ou non")
            reponse = input()

            while reponse == "oui" or reponse == "non":
                print("Réponse non accepté")
                reponse = input()

            if reponse == "oui":
                self.potion_vie = False
                print("Voici les morts du tour" + str(self.mort_tour))

        elif self.potion_mort == True :
            print("Voulez vous utiliser votre potion de mort, oui ou non")
            reponse = input()

            while reponse == "oui" or reponse == "non":
                print("Réponse non accepté")
                reponse = input()

            if reponse == "oui":
                self.potion_vie = False





    """Méthode permettant de créer le rôle voleur avec sa capacité à voler un role au premier tour
    paramètre : moment
    """
    def voleur(self):

        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        prenom = []
        for i in range(0, len(liste)):
            prenom.append(liste[i].get_prenom())

        print("Liste des joueurs dans la partie : " + str(prenom))

        print("Entrée le nom du joueur dont vous voulez voler le rôle ")
        indice = input()

        while indice not in liste:
            print("Ce joueur n'existe pas , veuillez renseigner un autre nom")
            indice = input()

        for i in liste :
            if liste[i].get_prenom() == indice:
                nouveau_role = liste[i].get_role()
                liste[i].set_role("Villageois")

        for i in liste:
            if liste[i].get_role() == "Voleur":
                liste[i].set_role(nouveau_role)
                print("Votre nouveau rôle est "+liste[i].get_role())




    """Méthode permettant de créer le rôle villageois
    paramètre : moment
    """
    def villageois(self):
        pass
    """Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour
    paramètre : moment
    """
    def voyante(self):

            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            prenom = []
            for i in range(0, len(liste)):
                prenom.append(liste[i].get_prenom())

            print("Liste des joueurs dans la partie : " + str(prenom))

            print("Entrée le nom du joueur dont vous voulez voir le rôle ")
            reponse = input()

            while reponse not in liste :
                print("Ce joueur n'existe pas , veuillez renseigner un autre nom")
                reponse = input()

            for i in liste :
                if liste[i].get_joueur() == reponse:
                    resultat = liste[i].get_role()
                    print("Le rôle de ce joueur est "+ resultat)



    """Méthode permettant de créer le rôle loup_garou où il votent la nuit
    paramètre : moment
    """
    def loup_garou(self):
        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        prenom = []
        for i in range(0,len(liste)):
            prenom.append(liste[i].get_prenom())

        print("Liste des joueurs dans la partie : " + str(prenom))

        print("Vote des autres loups"+ self.vote_loup)

        nombre_loup = len(self.loup)
        print("Pour qui veux tu voter")
        reponse = input()
        while reponse not in liste:
            print("Nom pas présent dans la liste, recommencer")
            reponse = input()
        if nombre_loup > 1:
            self.vote_loup.append(reponse)
            self.loup.pop(0)
            for i in range (0, len(liste)):
                if liste[i].get_prenom() == reponse :
                    liste[i].vote()

        if nombre_loup == 1:
            for i in range (0, len(liste)):
                if liste[i].get_prenom() == reponse :
                    liste[i].vote()

            max = 0
            indice = 0
            for i in range(0, len(liste)):
                if max < liste[i].get_vote():
                    max = liste[i].get_vote()
                    indice = i

            liste[indice].set_mort(True)
            if liste[indice].get_marier() == True:
                for i in range(0, len(liste)):
                    if liste[i].get_marie() == True:
                        liste[indice].set_mort(True)

        for i in range(0, len(liste)):
            liste[i].reset_vote()

    def demasquage_petite_fille(self):
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()

            # Créer une liste avec la petite fille
            fille = ""
            for joueur in liste:
                if joueur.get_role() == "Petite Fille":
                    fille = joueur.get_joueur().lower()
                    break

            # fréquence de chaque lettre
            lettre_freq = {}
            for joueur in liste:
                nom_joueur = joueur.get_joueur().lower()
                for lettre in nom_joueur:
                    lettre_freq[lettre] = lettre_freq.get(lettre, 0) + 1

            # liste de la petite fille sans lettres uniques
            fille_filtre = ""
            for lettre in fille:
                if lettre_freq[lettre] > 1:
                    fille_filtre += lettre

            if not self.lettre_petite_fille:
                self.lettre_petite_fille = [[] for i in fille]

            lettres_dispo = []
            for lettre in fille_filtre:
                if lettre not in self.lettre_petite_fille:
                    lettres_dispo.append(lettre)

            max_lettres = len(fille) // 2

            if lettres_dispo and len(self.lettre_petite_fille) < max_lettres:
                lettre = lettres_dispo[randint(0, len(lettres_dispo) - 1)]
                self.lettre_petite_fille.append(lettre)


    """
    Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoire des noms des loups-garous
    """

    def petite_fille(self):
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()

            # Affichage des noms des joueurs
            print("Liste des joueurs dans la partie : " +str(liste) )

            # Créer une liste des noms des Loups
            loups = []
            for joueur in liste:
                if joueur.get_role() == "Loup Garou":
                    loups.append(joueur.get_joueur().lower())

            # fréquence de chaque lettre
            lettre_freq = {}
            for joueur in liste:
                nom_joueur = joueur.get_joueur().lower()
                for lettre in nom_joueur:
                    lettre_freq[lettre] = lettre_freq.get(lettre, 0) + 1

            # liste noms des Loups sans lettres uniques
            loups_filtre = []
            for loup in loups:
                loup_filtre = ""
                for lettre in loup:
                    if lettre_freq[lettre] > 1:
                        loup_filtre += lettre
                loups_filtre.append(loup_filtre)

            # Initialiser self.lettre_loup_garou
            if not self.lettre_loup_garou:
                self.lettre_loup_garou = [[] for i in loups]

            # Sélectionner aléatoirement environ la moitié des Loups
            nombre_loups_a_afficher = len(loups) // 2
            indices_choisis = set()
            while len(indices_choisis) < nombre_loups_a_afficher:
                indices_choisis.add(randint(0, len(loups) - 1))

            #  une lettre aléatoire pour chaque Loup sélectionné
            for i in indices_choisis:
                lettres_dispo = []
                for lettre in loups_filtre[i]:
                    if lettre not in self.lettre_loup_garou[i]:
                        lettres_dispo.append(lettre)

                max_lettres = len(loups[i]) // 2

                if lettres_dispo and len(self.lettre_loup_garou[i]) < max_lettres:
                    lettre = lettres_dispo[randint(0, len(lettres_dispo) - 1)]
                    self.lettre_loup_garou[i].append(lettre)

            shuffle(liste)
            print(liste)
            # Affichage des lettres
            i = 0
            for lettres in self.lettre_loup_garou:
                if lettres:
                    print(f"Lettres pour le loup-garou '[i]': {', '.join(lettres)}")
                else:
                    print(f"Aucune lettre retournée pour le loup-garou '[i]'")
                i += 1

    """Méthode permettant de créer le rôle chasseur où quand il meurt il tue une personne qu'il choisit
    paramètre : moment
    """
    def chasseur(self):
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            for i in range (0, len(liste)):
                if liste[i].get_role() == "Chasseur" and liste[i]:
                    print("Voici la liste des noms de tous les joueurs :" + str(liste))
                    print("Qui voulez vous tuer")
                    reponse = input()
                    while reponse not in liste :
                        print("Nom pas présent dans la liste, recommencer")
                        reponse = input()

            for i in range(0,len(liste)):
                if liste[i].get_prenom == reponse:
                    liste[i].set_mort(True)
                    self.mort.append(liste[i].get_prenom())
                    self.mort_tour.append(liste[i].get_prenom())

                if liste[i].get_marier() == True:
                    for i in range(0, len(liste)):
                        if liste[i].get_marie() == True:
                            liste[i].set_mort(True)
                            self.mort.append(liste[i].get_prenom())
                            self.mort_tour.append(liste[i].get_prenom())


    """Méthode permettant de créer le rôle cupidon où il lie deux personnes et si une des deux meurts alors les deux meurts
    paramètre : moment
    """
    def cupidon(self):
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            print("Voici la liste des noms de tous les joueurs :" + str(liste))

            print("Quel est la première personne du couple ?")
            couple1 = input()
            while couple1 not in liste:
                print("Nom pas présent dans la liste, recommencer")
                couple1 = input()

            print("Quel est la deuxième personne du couple ?")
            couple2 = input()
            while couple2 not in liste or couple1 == couple2:
                print("Nom pas présent dans la liste, recommencer")
                couple2 = input()

            for i in range (0, len(liste)):

                if liste[i].get_prenom() == couple1 :
                    liste[i].set_marie(True)

                if liste[i].get_prenom() == couple2 :
                    liste[i].set_marie(True)

    """Méthode permettant de créer le rôle capitaine où il a vote double
    paramètre :
    """
    def capitaine(self):
        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()

        for i in range(0, len(liste)):
            if liste[i].get_mort() == True:
                liste[i].pop()
        print("Voici la liste des noms de tous les joueurs :" + str(liste))

        for i in range(0, len(liste)):
            print("Avez vous déja voté oui/non ")
            reponse = input()
            while reponse != "non":
                print("Ce n'est pas à vous de voter, passez la tablette à votre voisin")
                # clear screen
                print("Avez vous déja voté oui/non ")
                reponse = input()

            print("Pour qui voulez vous voter ?")
            reponse = input()
            while reponse not in liste:
                print("Nom pas présent dans la liste, recommencer")
                reponse = input()

            for i in range(0, len(liste)):
                if liste[i].get_prenom() == reponse:
                    liste[i].vote()
            print("Vous avez voté ")

        max = 0
        indice = 0
        for i in range(0, len(liste)):
            if max < liste[i].get_vote():
                max = liste[i].get_vote()
                indice = i

        liste[indice].set_maire(True)

        for i in range(0, len(liste)):
            liste[i].reset_vote()

    def vote(self):
        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()

        for i in range (0,len(liste)):
            if liste[i].get_mort() == True :
                liste[i].pop()
        print("Voici la liste des noms de tous les joueurs :" + str(liste))

        for i in range (0, len(liste)):
            print("Avez vous déja voté oui/non ")
            reponse = input()
            while reponse != "non" :
                print("Ce n'est pas à vous de voter, passez la tablette à votre voisin")
                # clear screen
                print("Avez vous déja voté oui/non ")
                reponse = input()

            print("Pour qui voulez vous voter ?")
            reponse = input()
            while reponse not in liste:
                print("Nom pas présent dans la liste, recommencer")
                reponse = input()

            for i in range (0, len(liste)):
                if liste[i].get_prenom() == reponse :
                    liste[i].vote()
            print("Vous avez voté ")
            #clear screen
        max = 0
        indice = 0
        for i in range (0, len(liste)):
            if max < liste[i].get_vote() :
                max = liste[i].get_vote()
                indice = i

        liste[indice].set_mort(True)
        self.mort.append(liste[indice].get_prenom())
        self.mort_tour.append(liste[indice].get_prenom())

        if liste[indice].get_marier() == True:
            for i in range (0, len(liste)):
                if liste[i].get_marie() == True:
                    liste[i].set_mort(True)
                    self.mort.append(liste[i].get_prenom())
                    self.mort_tour.append(liste[i].get_prenom())

        for i in range(0, len(liste)):
            liste[i].reset_vote()

    def afficher_mort(self):
        print("Les morts de ce tour sont : " + self.mort_tour)
        print("Les morts de la partie sont : " + self.mort)
        self.mort_tour = []

    def get_data(self):
        res = {
            "potion_vie" : self.potion_vie,
            "potion_mort" : self.potion_mort,
            "lettre_loup_garou" : self.lettre_loup_garou,
            "lettre_petite_fille" : self.lettre_petite_fille,
            "mort_tour" : self.mort_tour,
            "mort" : self.mort,
            "loup" : self.loup,
            "vote_loup" : self.vote_loup
        }

        return res

    def load_data(self, data : dict):
        self.potion_vie = data["potion_vie"]
        self.potion_mort = data["potion_mort"]
        self.lettre_loup_garout = data["lettre_loup_garout"]
        self.lettre_petite_fille = data["lettre_petite_fille"]
        self.mort_tour = data["mort_tour"]
        self.mort = data["mort"]
        self.loup = data["loup"]
        self.vote_loup = data["vote_loup"]
