from operator import xor
from random import *
import Affichage
import time


class Role():
    def __init__(self):

        self.potion_vie = True
        self.potion_mort = True
        self.lettre_loup_garou = []
        self.lettre_petite_fille = []
        self.mort_tour = []
        self.mort =[]
        self.loup = []
        self.vote_loup = []
        self.aff = Affichage.Affichage()



    def sorciere(self,joueurs):
        """
        Objectif : Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables
        Entrée : joueurs
        Sortie : Aucune
        """
        liste = []
        for i in range(0,len(joueurs)):
            if not xor(joueurs[i].get_prenom() != self.mort_tour[0], joueurs[i].get_mort != True):
                liste.append(joueurs[i])

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ","WHITE")
        self.aff.liste_joueurs(prenoms,[])

        self.aff.phrases("Voici le mort du tour", "WHITE")
        mort = []
        mort.append(self.mort_tour[0])
        self.aff.liste_joueurs(mort, [])

        if self.potion_vie == True:
            self.aff.phrases("Voulez vous utiliser votre potion de vie, oui ou non","WHITE")
            reponse = input().strip().lower()

            while reponse not in ["oui", "non"]:
                self.aff.phrases("Réponse non accepté, veuillez mettre oui ou non","WHITE")
                reponse = input().strip().lower()

            if reponse == "oui":
                self.potion_vie = False
                self.aff.phrases("Qui voulez vous ressusciter ?", "WHITE")
                reponse = input().strip()
                while reponse not in self.mort_tour :
                    self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
                    reponse = input().strip()

                for i in range(0, len(joueurs)):
                    if reponse == joueurs[i].get_prenom():
                        joueurs[i].set_mort(False)

                        if joueurs[i].get_marie() == True:
                            for i in range(0, len(joueurs)):
                                if joueurs[i].get_marie() == True:
                                    joueurs[i].set_mort(False)

                for i in range(0, len(self.mort)):
                    if reponse == joueurs[i].get_prenom():
                        self.mort.pop(i)


                self.mort_tour.pop(0)


                self.aff.phrases("Vous avez ressuscité "+reponse,"WHITE")
                # self.aff.sorciere(False, reponse, "vie")


        if self.potion_mort == True :
            self.aff.phrases("Voulez vous utiliser votre potion de mort, oui ou non","WHITE")
            reponse = input().strip().lower()

            while reponse not in ["oui", "non"]:
                self.aff.phrases("Réponse non accepté, veuillez mettre oui ou non","WHITE")
                reponse = input().strip().lower()


            if reponse == "oui":
                self.potion_mort = False
                self.aff.phrases("Qui voulez vous tuez ?","WHITE")
                reponse = input().strip()
                while reponse not in prenoms:
                    self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
                    reponse = input().strip()

                for i in range(0, len(joueurs)):
                    if reponse == joueurs[i].get_prenom():
                        joueurs[i].set_mort(True)
                        self.mort.append(joueurs[i].get_prenom())
                        self.mort_tour.append(joueurs[i].get_prenom())

                        if joueurs[i].get_marie() == True:
                            for i in range(0, len(joueurs)):
                                if joueurs[i].get_marie() == True:
                                    joueurs[i].set_mort(True)

                self.aff.phrases("Vous avez tué " + reponse,"WHITE")
                # self.aff.sorciere(False, reponse, "mort")

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()



    def voleur(self,joueurs,joueur_actuel):
        """
        Objectif : Méthode permettant de créer le rôle voleur avec sa capacité à voler un role au premier tour
        Entrée : joueurs, joueur_actuel
        Sortie : Aucune
        """

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        self.aff.phrases("Entrée le nom du joueur dont vous voulez voler le rôle ","WHITE")
        reponse = input().strip()

        while reponse not in prenoms:
            self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
            reponse = input().strip()

        nouveau_role = ""
        for i in range (len(joueurs)) :
            if joueurs[i].get_prenom() == reponse:
                nom = joueurs[i].get_prenom()
                nouveau_role = joueurs[i].get_role()
                joueurs[i].set_role('Simple Villageois')



        joueur_actuel.set_role(nouveau_role)

        self.aff.voleur(False)
        self.aff.phrases("Votre nouveau rôle est "+joueur_actuel.get_role(),"WHITE")

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()



    def voyante(self,joueurs):
        """
        Objectif : Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour
        Entrée : joueurs
        Sortie : Aucune
        """

        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        self.aff.phrases("Entrée le nom du joueur dont vous voulez voir le rôle ","WHITE")
        reponse = input().strip()

        while reponse not in prenoms :
            self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
            reponse = input().strip()


        for joueur in joueurs :
            if joueur.get_prenom() == reponse:
                resultat = joueur.get_role()
                self.aff.reinitialiser_screen()
                if resultat == "Cupidon":
                    self.aff.print_cards("./illustration/Cupidon.jpg")
                elif resultat == "Loup Garous":
                    self.aff.print_cards("./illustration/LG.jpg")
                elif resultat == "Voyante":
                    self.aff.print_cards("./illustration/Voyante.jpg")
                elif resultat == "Simple Villageois":
                    self.aff.print_cards("./illustration/Villageois.jpg")
                elif resultat == "Sorcière":
                    self.aff.print_cards("./illustration/Sorciere.jpg")
                elif resultat == "Petite Fille":
                    self.aff.print_cards("./illustration/Petite-Fille.jpg")
                elif resultat == "Chasseur":
                    self.aff.print_cards("./illustration/Chasseur.jpg")
                elif resultat == "Voleur":
                    self.aff.print_cards("./illustration/Voleur.jpg")

        self.aff.voyante(False, reponse)

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()


    def loup_garou(self,joueurs,joueur_actuel):
        """
        Objectif : Méthode permettant de créer le rôle loup_garou où ils votent la nuit
        Entrée : joueurs
        Sortie : Aucune
        """

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.loup = [joueurs.get_prenom() for joueurs in liste if joueurs.get_role() == "Loup Garous"]

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, self.loup)

        self.aff.phrases("Vote des autres loups :", "WHITE")
        self.aff.liste_joueurs(self.vote_loup, self.loup)

        nombre_loup = len(self.loup)
        nombre_vote = len(self.vote_loup)


        self.aff.phrases("Pour qui veux tu voter","WHITE")
        reponse = input().strip()
        while reponse not in prenoms:
            self.aff.phrases("Nom pas présent dans la liste, recommencez","WHITE")
            reponse = input().strip()

        if nombre_loup-1 > nombre_vote:
            self.vote_loup.append(reponse)
            self.loup.remove(joueur_actuel.get_prenom())
            for i in range (0, len(joueurs)):
                if joueurs[i].get_prenom() == reponse :
                    joueurs[i].vote()


        elif nombre_loup-1 == nombre_vote:
            for i in range (0, len(joueurs)):
                if joueurs[i].get_prenom() == reponse :
                    joueurs[i].vote()

            max = 0
            indice = 0
            for i in range(0, len(joueurs)):
                if max < joueurs[i].get_vote():
                    max = joueurs[i].get_vote()
                    indice = i
                elif max == joueurs[i].get_vote():
                    a = randint(0, 1)
                    if a == 0:
                        max = joueurs[i].get_vote()

            joueurs[indice].set_mort(True)
            self.vote_loup = []
            self.mort_tour.append(joueurs[indice].get_prenom())

            if joueurs[indice].get_marie() == True:
                for i in range(0, len(joueurs)):
                    if joueurs[i].get_marie() == True:
                        joueurs[i].set_mort(True)


            for i in range(0, len(joueurs)):
                joueurs[i].reset_vote()


        self.aff.loup_garou(False, reponse)

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()

    def demasquage_petite_fille(self,joueurs):
        """
        Objectif : Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoire des noms des loups-garous
        Entrée : joueurs
        Sortie : Aucune
        """
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Créer une liste avec la petite fille
        fille = ""
        for joueur in liste:
            if joueur.get_role() == "Petite Fille":
                fille = joueur.get_prenom().lower()

        # fréquence de chaque lettre
        lettre_freq = {}
        for joueur in joueurs:
            nom_joueur = joueur.get_prenom().lower()
            for lettre in nom_joueur:
                lettre_freq[lettre] = lettre_freq.get(lettre, 0) + 1

        # liste de la petite fille sans lettres uniques
        fille_filtre = ""
        for lettre in fille:
            if lettre_freq[lettre] > 1:
                fille_filtre += lettre

        if not self.lettre_petite_fille:
            self.lettre_petite_fille = []

        lettres_dispo = []
        for lettre in fille_filtre:
            if lettre not in self.lettre_petite_fille:
                lettres_dispo.append(lettre)

        max_lettres = len(fille) // 2

        if lettres_dispo and len(self.lettre_petite_fille) < max_lettres:
            lettre = lettres_dispo[randint(0, len(lettres_dispo) - 1)]
            self.lettre_petite_fille.append(lettre)


    def petite_fille(self,joueurs):
        """
        Objectif : Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoire des noms des loups-garous
        Entrée : joueurs
        Sortie : Aucune
        """
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        autre = prenoms [:]
        shuffle(autre)
        self.aff.liste_joueurs(autre, [])

        # Créer une liste des noms des Loups
        loups = []
        for joueur in liste:
            if joueur.get_role() == "Loup Garous":
                loups.append(joueur.get_prenom().lower())


        # fréquence de chaque lettre
        lettre_freq = {}
        for joueur in liste:
            nom_joueur = joueur.get_prenom().lower()
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


        # Affichage des lettres
        i = 1
        for lettres in self.lettre_loup_garou:
            if lettres:
                self.aff.phrases(f"Lettres pour le loup-garou {i}: {', '.join(lettres)}","WHITE")
            else:
                self.aff.phrases(f"Aucune lettre retournée pour le loup-garou {i}","WHITE")
            i += 1

        self.aff.petite_fille(False)

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()


    def chasseur(self,joueurs):
        """
        Objectif : Méthode permettant de créer le rôle chasseur où quand il meurt il tue une personne qu'il choisit
        Entrée : joueurs
        Sortie : Aucune
        """

        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        self.aff.phrases("Qui voulez vous tuer","WHITE")
        reponse = input().strip()
        while reponse not in prenoms :
            self.aff.phrases("Nom pas présent dans la liste, recommencez","WHITE")
            reponse = input().strip()

        for i in range(0,len(joueurs)):
            if reponse == joueurs[i].get_prenom() :
                joueurs[i].set_mort(True)
                self.mort.append(joueurs[i].get_prenom())
                self.mort_tour.append(joueurs[i].get_prenom())

                if joueurs[i].get_marie() == True:
                    for i in range(0, len(joueurs)):
                        if joueurs[i].get_marie() == True:
                            joueurs[i].set_mort(True)
                            self.mort.append(joueurs[i].get_prenom())


        self.aff.chasseur(False,reponse)

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()



    def cupidon(self,joueurs):
        """
        Méthode permettant de créer le rôle cupidon où il lie deux personnes et si une des deux meurts alors les deux meurts
        Objectif : joueurs
        Sortie : Aucune
        """
        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        self.aff.phrases("Quel est la première personne du couple ?","WHITE")
        couple1 = input()
        while couple1 not in prenoms :
            self.aff.phrases("Nom pas présent dans la liste, recommencer","WHITE")
            couple1 = input()

        self.aff.phrases("Quel est la deuxième personne du couple ?","WHITE")
        couple2 = input()
        while couple2 not in prenoms or couple1 == couple2:
            if couple1 == couple2:
                self.aff.phrases("Veuillez donner un nom différent du premier", "WHITE")
                couple2 = input()
            else :
                self.aff.phrases("Nom pas présent dans la liste, recommencer","WHITE")
                couple2 = input()

        for i in range (0, len(joueurs)):

            if joueurs[i].get_prenom() == couple1 :
                joueurs[i].set_marie(True)

            if joueurs[i].get_prenom() == couple2 :
                joueurs[i].set_marie(True)

        self.aff.cupidon(False, couple1, couple2)

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        self.aff.reinitialiser_screen()


    def capitaine(self,joueurs):
        """
        Objectif : Méthode permettant de créer le rôle capitaine où il a vote double
        Entrée : joueurs
        Sortie : Aucune
        """
        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.reinitialiser_screen()
        self.aff.afficher_texte("Il est dorénavant temps d'elire le maire !")
        time.sleep(3)
        self.aff.reinitialiser_screen()

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        for i in range(0, len(liste)):
            print("\n\n")
            self.aff.afficher_texte(joueurs[i].get_prenom())
            self.aff.phrases("\nPour qui voulez vous voter ?\n","WHITE")
            reponse = input()

            while reponse not in prenoms:
                self.aff.phrases("Nom pas présent dans la liste, recommencer","WHITE")
                reponse = input()

            for i in range(0, len(joueurs)):
                if joueurs[i].get_prenom() == reponse:
                    joueurs[i].vote()
            self.aff.phrases("Vous avez voté ","WHITE")

            self.aff.reinitialiser_screen()
            self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
            self.aff.liste_joueurs(prenoms, [])

        max = 0
        indice = 0
        for i in range(0, len(joueurs)):
            if max < joueurs[i].get_vote():
                max = joueurs[i].get_vote()
                indice = i

        joueurs[indice].set_maire(True)

        self.aff.capitaine(joueurs[indice].get_prenom())

        for i in range(0, len(joueurs)):
            joueurs[i].reset_vote()




    def afficher_mort_tour(self):
        """
        Objectif : Méthode permettant d'afficher les morts du tour
        Entrée : joueurs,joueur_actuel
        Sortie : Aucune
        """
        for i in self.mort_tour:
            self.aff.eliminer(i)
            self.aff.afficher_texte("Son role etait : " + i.get_role())
        self.mort_tour = []


    def get_mort_tour(self):
        return self.mort_tour

    def nouveau_maire(self,joueurs,joueur_actuel):
        """
        Objectif : Méthode permettant de choisir un nouveau maire
        Entrée : joueurs,joueur_actuel
        Sortie : Aucune
        """

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.reinitialiser_screen()

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        self.aff.afficher_texte(joueur.get_prenom())

        self.aff.phrases("Qui voulez vous choisir comme nouveau maire", "WHITE")
        reponse = input().strip()
        while reponse not in prenoms:
            self.aff.phrases("Nom pas présent dans la liste, recommencez", "WHITE")
            reponse = input().strip()

        for i in range (0, len(joueurs)):

            if joueurs[i].get_prenom() == reponse :
                joueurs[i].set_maire(True)

        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        joueur_actuel.set_maire(False)

        self.aff.reinitialiser_screen()

    def get_data(self):
        """
        Objeciif : Méthode permettant de retourner les données du rôle en JSON
        Entrée : Aucune
        Sortie : res
        """
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
        """
        Objectif : Méthode permettant de charger les données du rôle
        Entrée : data
        Sortie : Aucune
        """
        self.potion_vie = data["potion_vie"]
        self.potion_mort = data["potion_mort"]
        self.lettre_loup_garou = data["lettre_loup_garou"]
        self.lettre_petite_fille = data["lettre_petite_fille"]
        self.mort_tour = data["mort_tour"]
        self.mort = data["mort"]
        self.loup = data["loup"]
        self.vote_loup = data["vote_loup"]
