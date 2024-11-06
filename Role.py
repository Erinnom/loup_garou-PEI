from random import *
import LG_Affichage as affichage
import Joueur
import Partie
import random

class Role():
    def __init__(self):
        self.potion_vie = True
        self.potion_mort = True
        self.lettre_loup_garou = []
        self.lettre_petite_fille = ""

    """Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables 
    paramètre : moment
    """
    def sorciere(self,moment):
        if moment == "nuit" :
            if self.potion_vie == True:
                print("Voulez vous utiliser votre potion de vie, oui ou non")
                reponse = input()

                while reponse == "oui" or reponse == "non":
                    print("Réponse non accepté")
                    reponse = input()

                if reponse == "oui":
                    self.potion_vie = False

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

        vol = affichage.Affichage()
        vol.voleur(0,"joueur")
        indice = input("Entrée le nom du joueur dont vous voulez voler le rôle : ")
        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        nouveau_role = liste[indice].get_role()
        liste[indice].set_role("Villageois")

        for i in liste:
            if liste[i].get_role() == "Voleur":
                liste[i].set_role(nouveau_role)
                print("Votre nouveau rôle est "+liste[i].get_role())




    """Méthode permettant de créer le rôle villageois 
    paramètre : moment
    """
    def villageois(self,moment):
        pass
    """Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour 
    paramètre : moment
    """
    def voyante(self,moment):
        if moment == "nuit" :
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            print("")
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
    def loup_garou(self,moment,joueur):
        pass

    def demasquage_petite_fille(self,moment):
        if moment == "nuit":
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

    def petite_fille(self, moment):
        if moment == "nuit":
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()

            # Affichage des noms des joueurs
            print("Liste des joueurs dans la partie :")

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

            # liste noms des Loups san lettres uniques
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
    def chasseur(self,moment):
        if moment == "nuit":
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            for i in range (0, len(liste)):
                if liste[i].get_role() == "Chasseur" and liste[i]:
                    print("Voici la liste des noms de tous les joueurs :" + liste)
                    print("Qui voulez vous tuer")
                    reponse = input()
                    if reponse not in liste:
                        print("Nom pas présent dans la liste, recommencer")
                        reponse = input()


    """Méthode permettant de créer le rôle cupidon où il lie deux personnes et si une des deux meurts alors les deux meurts 
    paramètre : moment
    """
    def cupidon(self,moment):
        if moment == "nuit":
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            print("Voici la liste des noms de tous les joueurs :" + liste)

    """Méthode permettant de créer le rôle capitaine où il a vote double 
    paramètre : 
    """
    def capitaine(self,moment):
        if moment == "nuit":
            pass

    def vote(self):
        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        print("Voici la liste des noms de tous les joueurs :" + liste)