from random import *
import Affichage

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


    """Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables
    paramètre : moment
    """
    def sorciere(self,joueurs):
        self.aff.sorciere(True,"")
        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ","WHITE")
        self.aff.liste_joueurs(prenoms,[])

        if self.potion_vie == True:
            self.aff.phrases("Voulez vous utiliser votre potion de vie, oui ou non","WHITE")
            reponse = input().strip().lower()

            while reponse not in ["oui", "non"]:
                self.aff.phrases("Réponse non accepté","WHITE")
                reponse = input().strip().lower()

            if reponse == "oui":
                self.potion_vie = False
                self.aff.phrases("Voici les morts du tour","WHITE")
                self.aff.liste_joueurs(self.mort_tour,self.mort_tour)

                self.aff.phrases("Qui voulez vous ressusciter ?","WHITE")
                reponse = input().strip()
                while reponse not in self.mort_tour :
                    self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
                    reponse = input().strip()

                for i in range(0, len(liste)):
                    if reponse == liste[i].get_prenom():
                        liste[i].get_mort(False)


                self.mort_tour.remove(reponse)
                self.mort.remove(reponse)

                self.aff.phrases("Vous avez ressuscité "+reponse,"WHITE")
                self.aff.sorciere(False, reponse, "vie")


        if self.potion_mort == True :
            self.aff.phrases("Voulez vous utiliser votre potion de mort, oui ou non","WHITE")
            reponse = input().strip().lower()

            while reponse not in ["oui", "non"]:
                self.aff.phrases("Réponse non accepté","WHITE")
                reponse = input().strip().lower()


            if reponse == "oui":
                self.potion_mort = False
                self.aff.phrases("Qui voulez vous tuez ?","WHITE")
                reponse = input().strip()
                while reponse not in prenoms:
                    self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
                    reponse = input().strip()

                for i in range(0, len(liste)):
                    if reponse == liste[i].get_prenom():
                        liste[i].get_mort(True)
                        self.mort.append(liste[i].get_prenom())
                        self.mort_tour.append(liste[i].get_prenom())

                self.aff.phrases("Vous avez tué " + reponse,"WHITE")
                self.aff.sorciere(False, reponse, "mort")

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()


    """Méthode permettant de créer le rôle voleur avec sa capacité à voler un role au premier tour
    paramètre : moment
    """
    def voleur(self,joueurs,joueur_actuel):

        self.aff.voleur(True,"")

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
        indice = input().strip()

        while indice not in prenoms:
            self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom","WHITE")
            indice = input().strip()

        nouveau_role = ""
        for i in liste :
            if liste[i].get_prenom() == indice:
                role = liste[i].get_prenom()
                nouveau_role = liste[i].get_role()
                liste[i].set_role("Villageois")

                self.aff.voleur(False,role)


        joueur_actuel.set_role(nouveau_role)
        self.aff.phrases("Votre nouveau rôle est "+joueur_actuel.get_role(),"WHITE")

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()

    """Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour"""

    def villageois(self,joueurs,joueur_actuel):
        self.aff.villageois()

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        couple =""
        if joueur_actuel.get_marie() == True :
            for i in range (len(liste)):
                if liste[i].get_marie()==True and liste[i]!=joueur_actuel.get_prenom() :
                    couple += liste[i].get_prenom()
            self.aff.phrases("Vous êtes en couple avec "+couple,"WHITE")

        if joueur_actuel.get_maire() == True :
            self.aff.phrases("Vous êtes maire", "WHITE")

        self.aff.phrases("Vous n'avez rien à faire, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()


    """Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour
    """
    def voyante(self,joueurs):

        self.aff.voyante(True,"")

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

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

        self.aff.voyante(True,reponse)

        for i in liste :
            if i.get_prenom() == reponse:
                resultat = i.get_role()
                self.aff.phrases("Le rôle de ce joueur est "+ resultat,"WHITE")

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()



    """Méthode permettant de créer le rôle loup_garou où il votent la nuit
    paramètre : joueurs
    """
    def loup_garou(self,joueurs,joueur_actuel):

        self.aff.loup_garou(True,"")

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())
        print(prenoms)

        couple = ""
        if joueur_actuel.get_marie() == True:
            for i in range(len(liste)):
                if liste[i].get_marie() == True and liste[i] != joueur_actuel.get_prenom():
                    couple += liste[i].get_prenom()
            self.aff.phrases("Vous êtes en couple avec " + couple, "WHITE")

        if joueur_actuel.get_maire() == True:
            self.aff.phrases("Vous êtes maire", "WHITE")

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

        if nombre_vote < nombre_loup :
            self.vote_loup.append(reponse)
            for i in range (0, len(liste)):
                if liste[i].get_prenom() == reponse :
                    liste[i].vote()

        elif nombre_vote == nombre_loup - 1:
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
            self.aff.loup_garou(False, liste[indice].get_prenom())

            if liste[indice].get_marier() == True:
                for i in range(0, len(liste)):
                    if liste[i].get_marie() == True:
                        liste[indice].set_mort(True)

            for i in range(0, len(liste)):
                liste[i].reset_vote()


        self.aff.phrases("Vous avez voté : "+ reponse, "WHITE")


        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()

    def demasquage_petite_fille(self,joueurs):
        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        # Créer une liste avec la petite fille
        fille = ""
        for joueur in liste:
            if joueur.get_role() == "Petite Fille":
                fille = joueur.get_prenom().lower()

        # fréquence de chaque lettre
        lettre_freq = {}
        for joueur in liste:
            nom_joueur = joueur.get_prenom().lower()
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

    def petite_fille(self,joueurs):

        self.aff.petite_fille(True)

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

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

        autre = shuffle(liste)
        print(autre)
        # Affichage des lettres
        self.aff.petite_fille(False)
        i = 0
        for lettres in self.lettre_loup_garou:
            if lettres:
                self.aff.phrases(f"Lettres pour le loup-garou '[i]': {', '.join(lettres)}","WHITE")
            else:
                self.aff.phrases("Aucune lettre retournée pour le loup-garou '[i]'","WHITE")
            i += 1

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()

    """Méthode permettant de créer le rôle chasseur où quand il meurt il tue une personne qu'il choisit
    paramètre : moment
    """
    def chasseur(self,joueurs):

        self.aff.chasseur(True,"")

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

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

        self.aff.chasseur(False,reponse)
        self.aff.phrases("Vous avez tué : "+reponse, "WHITE")

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

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()


    """Méthode permettant de créer le rôle cupidon où il lie deux personnes et si une des deux meurts alors les deux meurts
    paramètre : moment
    """
    def cupidon(self,joueurs):

        self.aff.cupidon(True,"","")

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
        while couple1 not in liste:
            self.aff.phrases("Nom pas présent dans la liste, recommencer","WHITE")
            couple1 = input()

        self.aff.phrases("Quel est la deuxième personne du couple ?","WHITE")
        couple2 = input()
        while couple2 not in liste or couple1 == couple2:
            self.aff.phrases("Nom pas présent dans la liste, recommencer","WHITE")
            couple2 = input()

        for i in range (0, len(liste)):

            if liste[i].get_prenom() == couple1 :
                liste[i].set_marie(True)

            if liste[i].get_prenom() == couple2 :
                liste[i].set_marie(True)

        self.aff.cupidon(False,couple1,couple2)
        self.aff.phrases("Le couple est "+couple1+" et "+couple2, "WHITE")

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        self.aff.reinitialiser_screen()

    """Méthode permettant de créer le rôle capitaine où il a vote double
    paramètre :
    """
    def capitaine(self,joueurs):
        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        for i in range(0, len(liste)):
            self.aff.phrases("Avez vous déja voté oui/non ","WHITE")
            reponse = input()
            while reponse != "non":
                self.aff.phrases("Ce n'est pas à vous de voter, passez la tablette à votre voisin","WHITE")
                self.aff.phrases("Avez vous déja voté oui/non ","WHITE")
                reponse = input()

            self.aff.phrases("Pour qui voulez vous voter ?","WHITE")
            reponse = input()
            while reponse not in liste:
                self.aff.phrases("Nom pas présent dans la liste, recommencer","WHITE")
                reponse = input()

            for i in range(0, len(liste)):
                if liste[i].get_prenom() == reponse:
                    liste[i].vote()
            self.aff.phrases("Vous avez voté ","WHITE")

            self.aff.reinitialiser_screen()
            self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
            self.aff.liste_joueurs(prenoms, prenoms)

        max = 0
        indice = 0
        for i in range(0, len(liste)):
            if max < liste[i].get_vote():
                max = liste[i].get_vote()
                indice = i

        liste[indice].set_maire(True)

        for i in range(0, len(liste)):
            liste[i].reset_vote()


    def afficher_mort_tour(self,joueurs,joueur_actuel):
        self.aff.phrases("Les morts de ce tour sont : ","WHITE")
        self.aff.liste_joueurs(self.mort_tour, self.mort_tour)
        self.mort_tour = []

    def nouveau_maire(self,joueurs,joueur_actuel):

        self.aff.capitaine("")

        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        self.aff.phrases("Qui voulez vous choisir comme nouveau maire", "WHITE")
        reponse = input().strip()
        while reponse not in prenoms:
            self.aff.phrases("Nom pas présent dans la liste, recommencez", "WHITE")
            reponse = input().strip()

        for i in range (0, len(liste)):

            if liste[i].get_prenom() == reponse :
                liste[i].set_maire(True)

        self.aff.phrases("Vous avez fini votre tour, écrirez oui pour finir votre tour", "WHITE")
        effacer = input().strip()
        while effacer != "oui":
            self.aff.phrases("Veuillez écrire oui", "WHITE")
            effacer = input().strip()

        joueur_actuel.set_maire(False)

        self.aff.reinitialiser_screen()

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
        self.lettre_loup_garou = data["lettre_loup_garou"]
        self.lettre_petite_fille = data["lettre_petite_fille"]
        self.mort_tour = data["mort_tour"]
        self.mort = data["mort"]
        self.loup = data["loup"]
        self.vote_loup = data["vote_loup"]
