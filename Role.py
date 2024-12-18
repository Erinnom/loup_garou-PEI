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

    def sorciere(self, joueurs):
        """
        Objectif : Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables
        Entrée : joueurs
        Sortie : Aucune
        """
        # Initialisation d'une liste pour stocker les joueurs qui ne sont ni morts ni désignés comme la victime du tour
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Création d'une liste contenant uniquement les prénoms des joueurs valides
        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Affichage des joueurs encore en vie
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Affichage du joueur désigné comme victime pour ce tour
        self.aff.phrases("Voici le mort du tour", "WHITE")
        mort = []
        mort.append(self.mort_tour[0])
        self.aff.liste_joueurs(mort, [])

        # Si la potion de vie est disponible
        if self.potion_vie == True:
            self.aff.phrases("Voulez vous utiliser votre potion de vie, oui ou non", "WHITE")
            reponse = input().strip().lower()

            # Validation de la réponse utilisateur
            while reponse not in ["oui", "non"]:
                self.aff.phrases("Réponse non accepté, veuillez mettre oui ou non", "WHITE")
                reponse = input().strip().lower()

            # Si l'utilisateur décide d'utiliser la potion de vie
            if reponse == "oui":
                self.potion_vie = False  # La potion de vie est désormais utilisée
                self.aff.phrases("Qui voulez vous ressusciter ?", "WHITE")
                reponse = input().strip()

                # Validation du nom du joueur à ressusciter
                while reponse not in self.mort_tour:
                    self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom", "WHITE")
                    reponse = input().strip()

                # Résurrection du joueur désigné
                for i in range(0, len(joueurs)):
                    if reponse == joueurs[i].get_prenom():
                        joueurs[i].set_mort(False)  # Le joueur n'est plus mort

                        # Si le joueur ressuscité est marié, son partenaire est également ressuscité
                        if joueurs[i].get_marie() == True:
                            for i in range(0, len(joueurs)):
                                if joueurs[i].get_marie() == True:
                                    joueurs[i].set_mort(False)

                # Retrait du joueur ressuscité des listes des morts
                for i in range(0, len(self.mort)):
                    if reponse == joueurs[i].get_prenom():
                        self.mort.pop(i)

                self.mort_tour.pop(0)  # Le mort du tour est enlevé

                self.aff.phrases("Vous avez ressuscité " + reponse, "WHITE")
                # Ligne commentée : mise à jour graphique potentielle
                # self.aff.sorciere(False, reponse, "vie")

        # Si la potion de mort est disponible
        if self.potion_mort == True:
            self.aff.phrases("Voulez vous utiliser votre potion de mort, oui ou non", "WHITE")
            reponse = input().strip().lower()

            # Validation de la réponse utilisateur
            while reponse not in ["oui", "non"]:
                self.aff.phrases("Réponse non accepté, veuillez mettre oui ou non", "WHITE")
                reponse = input().strip().lower()

            # Si l'utilisateur décide d'utiliser la potion de mort
            if reponse == "oui":
                self.potion_mort = False  # La potion de mort est désormais utilisée
                self.aff.phrases("Qui voulez vous tuez ?", "WHITE")
                reponse = input().strip()

                # Validation du nom du joueur à tuer
                while reponse not in prenoms:
                    self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom", "WHITE")
                    reponse = input().strip()

                # Mise à jour des statuts pour le joueur désigné
                for i in range(0, len(joueurs)):
                    if reponse == joueurs[i].get_prenom():
                        joueurs[i].set_mort(True)  # Le joueur est désormais mort
                        self.mort.append(joueurs[i].get_prenom())
                        self.mort_tour.append(joueurs[i].get_prenom())

                        # Si le joueur tué est marié, son partenaire est également tué
                        if joueurs[i].get_marie() == True:
                            for i in range(0, len(joueurs)):
                                if joueurs[i].get_marie() == True:
                                    joueurs[i].set_mort(True)

                self.aff.phrases("Vous avez tué " + reponse, "WHITE")

        # Fin du tour de la sorcière
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialisation de l'écran après le tour
        self.aff.reinitialiser_screen()

    def voleur(self, joueurs, joueur_actuel):
        """
        Objectif : Méthode permettant de créer le rôle voleur avec sa capacité à voler un rôle au premier tour
        Entrée : joueurs, joueur_actuel
        Sortie : Aucune
        """

        # Création d'une liste des joueurs qui ne sont pas morts
        liste = []
        for joueur in joueurs:
            if not joueur.get_mort():  # On vérifie si le joueur est vivant
                liste.append(joueur)

        # Création d'une liste contenant les prénoms des joueurs vivants
        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Affichage de la liste des joueurs encore en vie
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Demande au voleur de choisir un joueur dont voler le rôle
        self.aff.phrases("Entrée le nom du joueur dont vous voulez voler le rôle ", "WHITE")
        reponse = input().strip()

        # Validation du choix, pour s'assurer que le prénom saisi existe
        while reponse not in prenoms:
            self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom", "WHITE")
            reponse = input().strip()

        # Initialisation de la variable pour stocker le rôle volé
        nouveau_role = ""
        for i in range(len(joueurs)):
            if joueurs[i].get_prenom() == reponse:
                # Récupération du prénom et du rôle du joueur sélectionné
                nom = joueurs[i].get_prenom()
                nouveau_role = joueurs[i].get_role()

                # Modification du rôle du joueur sélectionné en "Simple Villageois"
                joueurs[i].set_role('Simple Villageois')

        # Assignation du rôle volé au joueur actuel
        joueur_actuel.set_role(nouveau_role)

        # Mise à jour graphique pour indiquer que l'action du voleur est terminée
        self.aff.voleur(False)

        # Affichage du nouveau rôle attribué au voleur
        self.aff.afficher_texte("Votre nouveau rôle est " + joueur_actuel.get_role())

        # Fin du tour du voleur
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialisation de l'écran après le tour
        self.aff.reinitialiser_screen()

    def voyante(self, joueurs):
        """
        Objectif : Méthode permettant de créer le rôle voyante avec sa capacité à voir un rôle d'une personne chaque tour
        Entrée : joueurs
        Sortie : Aucune
        """

        # Création d'une liste des joueurs valides (ceux qui ne sont pas morts ni désignés comme mort du tour)
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Création d'une liste contenant les prénoms des joueurs valides
        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Affichage de la liste des joueurs disponibles pour la voyante
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Demande au joueur (voyante) de choisir un joueur pour voir son rôle
        self.aff.phrases("Entrée le nom du joueur dont vous voulez voir le rôle ", "WHITE")
        reponse = input().strip()

        # Validation de l'entrée : s'assurer que le prénom existe dans la liste
        while reponse not in prenoms:
            self.aff.phrases("Ce joueur n'existe pas , veuillez renseigner un autre nom", "WHITE")
            reponse = input().strip()

        # Recherche du joueur choisi et affichage de son rôle
        for joueur in joueurs:
            if joueur.get_prenom() == reponse:
                resultat = joueur.get_role()  # Obtient le rôle du joueur sélectionné
                self.aff.reinitialiser_screen()  # Réinitialise l'écran pour afficher uniquement le résultat

                # Affichage de la carte correspondante au rôle révélé
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

        # Mise à jour graphique pour indiquer que l'action de la voyante est terminée
        self.aff.voyante(False, reponse)

        # Indication de fin de tour de la voyante
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialisation de l'écran après le tour
        self.aff.reinitialiser_screen()

    def loup_garou(self, joueurs, joueur_actuel):
        """
        Objectif : Méthode permettant de créer le rôle loup_garou où ils votent la nuit
        Entrée : joueurs, joueur_actuel
        Sortie : Aucune
        """

        # Si le nombre de joueurs est supérieur à 9, affichage d'une liste spécifique pour traquer la petite fille
        if len(joueurs) > 9:
            self.aff.phrases("Liste pour démasquer la petite fille : ", "WHITE")
            self.aff.liste_joueurs(self.lettre_petite_fille, [])

        # Création d'une liste de joueurs valides (pas morts ni désignés comme morts ce tour)
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Extraction des prénoms des joueurs vivants
        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Création d'une liste des noms des loups-garous
        self.loup = [joueurs.get_prenom() for joueurs in liste if joueurs.get_role() == "Loup Garous"]

        # Affichage de la liste des joueurs encore en jeu
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, self.loup)

        # Affichage des votes des autres loups-garous
        self.aff.phrases("Vote des autres loups :", "WHITE")
        self.aff.liste_joueurs(self.vote_loup, self.loup)

        # Comptage des loups-garous et des votes exprimés
        nombre_loup = len(self.loup)
        nombre_vote = len(self.vote_loup)

        # Demande au joueur de voter pour un autre joueur
        self.aff.phrases("Pour qui veux tu voter", "WHITE")
        reponse = input().strip()

        # Validation du choix pour s'assurer que le nom est dans la liste
        while reponse not in prenoms:
            self.aff.phrases("Nom pas présent dans la liste, recommencez", "WHITE")
            reponse = input().strip()

        # Cas où tous les loups n'ont pas encore voté
        if nombre_loup - 1 > nombre_vote:
            self.vote_loup.append(reponse)  # Ajout du vote à la liste
            self.loup.remove(joueur_actuel.get_prenom())  # Retirer le joueur actuel de la liste des loups ayant voté
            for i in range(0, len(joueurs)):
                if joueurs[i].get_prenom() == reponse:
                    joueurs[i].vote()  # Ajout d'un vote au joueur sélectionné

        # Cas où tous les loups ont voté
        elif nombre_loup - 1 == nombre_vote:
            for i in range(0, len(joueurs)):
                if joueurs[i].get_prenom() == reponse:
                    joueurs[i].vote()  # Ajout d'un vote au joueur sélectionné

            # Détermination du joueur ayant reçu le plus de votes
            max = 0
            indice = 0
            for i in range(0, len(joueurs)):
                if max < joueurs[i].get_vote():
                    max = joueurs[i].get_vote()
                    indice = i
                elif max == joueurs[i].get_vote():
                    a = randint(0, 1)  # Cas d'égalité, tirage au sort
                    if a == 0:
                        max = joueurs[i].get_vote()

            # Le joueur ayant reçu le plus de votes est éliminé
            joueurs[indice].set_mort(True)
            self.vote_loup = []  # Réinitialisation des votes des loups
            self.mort_tour.append(joueurs[indice].get_prenom())  # Ajout du joueur éliminé à la liste des morts

            # Si le joueur éliminé est marié, son conjoint est également éliminé
            if joueurs[indice].get_marie() == True:
                for i in range(0, len(joueurs)):
                    if joueurs[i].get_marie() == True:
                        joueurs[i].set_mort(True)

            # Réinitialisation des votes pour tous les joueurs
            for i in range(0, len(joueurs)):
                joueurs[i].reset_vote()

        # Mise à jour graphique pour indiquer la fin du tour des loups-garous
        self.aff.loup_garou(False, reponse)

        # Fin du tour des loups-garous
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialisation de l'écran pour poursuivre le jeu
        self.aff.reinitialiser_screen()

    def demasquage_petite_fille(self, joueurs):
        """
        Objectif : Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoires des noms des loups-garous
        Entrée : joueurs
        Sortie : Aucune
        """

        # Création d'une liste filtrée des joueurs encore en vie et non désignés comme morts au tour actuel
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Recherche de la "Petite Fille" dans la liste des joueurs
        fille = ""
        for joueur in liste:
            if joueur.get_role() == "Petite Fille":  # Identifie le rôle "Petite Fille"
                fille = joueur.get_prenom().lower()  # Stocke son prénom en minuscules pour traitement des lettres

        # Création d'une fréquence des lettres présentes dans les noms des joueurs
        lettre_freq = {}
        for joueur in joueurs:
            nom_joueur = joueur.get_prenom().lower()  # Conversion en minuscules pour cohérence
            for lettre in nom_joueur:  # Parcourt chaque lettre du prénom
                lettre_freq[lettre] = lettre_freq.get(lettre, 0) + 1  # Comptabilise la fréquence de chaque lettre

        # Création d'une version du prénom de la "Petite Fille" sans lettres uniques
        fille_filtre = ""
        for lettre in fille:
            if lettre_freq[lettre] > 1:  # Seules les lettres présentes dans plusieurs noms sont retenues
                fille_filtre += lettre

        # Initialisation de la liste des lettres découvertes si elle n'existe pas encore
        if not self.lettre_petite_fille:
            self.lettre_petite_fille = []

        # Création d'une liste des lettres filtrées encore non révélées à la "Petite Fille"
        lettres_dispo = []
        for lettre in fille_filtre:
            if lettre not in self.lettre_petite_fille:  # Filtre les lettres déjà connues
                lettres_dispo.append(lettre)

        # Calcul du nombre maximum de lettres que la "Petite Fille" peut obtenir
        max_lettres = len(fille) // 2  # Le maximum est la moitié du prénom de la "Petite Fille"

        # Ajout d'une lettre aléatoire à la liste des lettres découvertes si les conditions sont remplies
        if lettres_dispo and len(self.lettre_petite_fille) < max_lettres:
            lettre = lettres_dispo[
                randint(0, len(lettres_dispo) - 1)]  # Sélectionne une lettre aléatoire parmi les disponibles
            self.lettre_petite_fille.append(lettre)  # Ajoute cette lettre à la liste des lettres découvertes

    def petite_fille(self, joueurs):
        """
        Objectif : Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoires
                   des noms des loups-garous.
        Entrée : joueurs
        Sortie : Aucune
        """

        # Appelle une méthode pour désactiver une vue ou une fonction associée à la petite fille.
        self.aff.petite_fille(False)

        # Liste des joueurs encore en jeu (excluant les morts ou ceux marqués comme non vivants).
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Extraction des prénoms des joueurs encore en jeu.
        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Affiche la liste des joueurs toujours dans la partie de manière mélangée.
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        autre = prenoms[:]  # Copie de la liste des prénoms.
        shuffle(autre)  # Mélange aléatoire des prénoms.
        self.aff.liste_joueurs(autre, [])

        # Création d'une liste contenant uniquement les noms des joueurs qui sont des loups-garous.
        loups = []
        for joueur in liste:
            if joueur.get_role() == "Loup Garous":
                loups.append(joueur.get_prenom().lower())

        # Création d'un dictionnaire pour compter la fréquence de chaque lettre apparaissant dans les prénoms.
        lettre_freq = {}
        for joueur in liste:
            nom_joueur = joueur.get_prenom().lower()
            for lettre in nom_joueur:
                lettre_freq[lettre] = lettre_freq.get(lettre, 0) + 1

        # Filtrage des noms des loups-garous pour ne garder que les lettres apparaissant plus d'une fois.
        loups_filtre = []
        for loup in loups:
            loup_filtre = ""
            for lettre in loup:
                if lettre_freq[lettre] > 1:  # Vérifie si la lettre apparaît plus d'une fois.
                    loup_filtre += lettre
            loups_filtre.append(loup_filtre)

        # Initialisation de l'attribut self.lettre_loup_garou s'il n'existe pas encore.
        if not self.lettre_loup_garou:
            self.lettre_loup_garou = [[] for i in loups]

        # Sélection aléatoire d'environ la moitié des loups-garous à afficher.
        nombre_loups_a_afficher = len(loups) // 2
        indices_choisis = set()  # Ensemble des indices des loups-garous sélectionnés.
        while len(indices_choisis) < nombre_loups_a_afficher:
            indices_choisis.add(randint(0, len(loups) - 1))

        # Sélection aléatoire de lettres à afficher pour chaque loup-garou sélectionné.
        for i in indices_choisis:
            lettres_dispo = []  # Liste des lettres encore disponibles pour ce loup.
            for lettre in loups_filtre[i]:
                if lettre not in self.lettre_loup_garou[i]:
                    lettres_dispo.append(lettre)

            max_lettres = len(loups[i]) // 2  # Limite du nombre de lettres à révéler (moitié du prénom).

            # Ajout d'une lettre aléatoire parmi les lettres disponibles.
            if lettres_dispo and len(self.lettre_loup_garou[i]) < max_lettres:
                lettre = lettres_dispo[randint(0, len(lettres_dispo) - 1)]
                self.lettre_loup_garou[i].append(lettre)

        # Affichage des lettres sélectionnées pour chaque loup-garou.
        i = 1
        for lettres in self.lettre_loup_garou:
            if lettres:
                self.aff.phrases(f"Lettres pour le loup-garou {i}: {', '.join(lettres)}", "WHITE")
            else:
                self.aff.phrases(f"Aucune lettre retournée pour le loup-garou {i}", "WHITE")
            i += 1

        # Invite à continuer après avoir affiché les informations.
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialisation de l'écran après la fin du tour.
        self.aff.reinitialiser_screen()

    def chasseur(self, joueurs):
        """
        Objectif : Méthode permettant de gérer le rôle du chasseur. Quand il meurt, il tue une personne qu'il choisit.
        Entrée : joueurs (liste d'objets représentant les joueurs)
        Sortie : Aucune
        """

        # Création d'une liste des joueurs encore en jeu (exclut les joueurs morts ou le joueur mort ce tour).
        liste = []
        for i in range(0, len(joueurs)):
            if not joueurs[i].get_prenom() == self.mort_tour or joueurs[i].get_mort != True:
                liste.append(joueurs[i])

        # Extraction des prénoms des joueurs encore en jeu.
        prenoms = []
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Affiche la liste des joueurs toujours en jeu.
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Invite le chasseur à choisir un joueur à tuer.
        self.aff.phrases("Qui voulez vous tuer", "WHITE")
        reponse = input().strip()

        # Vérifie que le prénom saisi est bien dans la liste des joueurs disponibles.
        while reponse not in prenoms:
            self.aff.phrases("Nom pas présent dans la liste, recommencez", "WHITE")
            reponse = input().strip()

        # Trouve le joueur correspondant au prénom choisi et le marque comme mort.
        for i in range(0, len(joueurs)):
            if reponse == joueurs[i].get_prenom():
                joueurs[i].set_mort(True)  # Marque le joueur comme mort.
                self.mort.append(joueurs[i].get_prenom())  # Ajoute le prénom du joueur à la liste des morts.
                self.mort_tour.append(joueurs[i].get_prenom())  # Ajoute le prénom à la liste des morts de ce tour.

                # Si le joueur mort est marié (lié à un autre joueur), tue aussi son partenaire.
                if joueurs[i].get_marie() == True:
                    for i in range(0, len(joueurs)):
                        if joueurs[i].get_marie() == True:
                            joueurs[i].set_mort(True)  # Marque le partenaire comme mort.
                            self.mort.append(joueurs[i].get_prenom())  # Ajoute son prénom à la liste des morts.

        # Désactive l'état "chasseur" et enregistre la cible choisie.
        self.aff.chasseur(False, reponse)

        # Invite le joueur à continuer après avoir choisi sa cible.
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialise l'écran après la fin du tour.
        self.aff.reinitialiser_screen()

    def cupidon(self, joueurs):
        """
        Méthode permettant de créer le rôle cupidon où il lie deux personnes, et si une des deux meurt, alors les deux meurent.
        Objectif : joueurs (liste d'objets représentant les joueurs)
        Sortie : Aucune
        """
        liste = []
        # Filtrer les joueurs qui ne sont pas morts pour les inclure dans la sélection
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        # Récupérer les prénoms des joueurs non morts
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Afficher la liste des joueurs encore en vie
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Demander à l'utilisateur de sélectionner le premier membre du couple
        self.aff.phrases("Quel est la première personne du couple ?", "WHITE")
        couple1 = input()
        while couple1 not in prenoms:
            # Vérifier si le prénom est valide, sinon redemander
            self.aff.phrases("Nom pas présent dans la liste, recommencer", "WHITE")
            couple1 = input()

        # Demander à l'utilisateur de sélectionner le deuxième membre du couple
        self.aff.phrases("Quel est la deuxième personne du couple ?", "WHITE")
        couple2 = input()
        while couple2 not in prenoms or couple1 == couple2:
            if couple1 == couple2:
                # Empêcher de choisir la même personne pour les deux membres du couple
                self.aff.phrases("Veuillez donner un nom différent du premier", "WHITE")
                couple2 = input()
            else:
                # Vérifier si le prénom est valide, sinon redemander
                self.aff.phrases("Nom pas présent dans la liste, recommencer", "WHITE")
                couple2 = input()

        # Marquer les deux joueurs comme étant "mariés" dans la liste des joueurs
        for i in range(0, len(joueurs)):
            if joueurs[i].get_prenom() == couple1:
                joueurs[i].set_marie(True)

            if joueurs[i].get_prenom() == couple2:
                joueurs[i].set_marie(True)

        # Afficher un message confirmant le rôle Cupidon et les joueurs sélectionnés
        self.aff.cupidon(False, couple1, couple2)

        # Informer que le tour est terminé et attendre une entrée utilisateur
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()

        # Réinitialiser l'écran pour préparer l'affichage suivant
        self.aff.reinitialiser_screen()

    def capitaine(self, joueurs):
        """
        Objectif : Méthode permettant de créer le rôle capitaine, où le capitaine a un vote double.
        Entrée : joueurs (liste d'objets représentant les joueurs)
        Sortie : Aucune
        """
        liste = []
        # Filtrer les joueurs qui ne sont pas morts pour les inclure dans la sélection
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        # Récupérer les prénoms des joueurs non morts
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Réinitialiser l'écran et afficher un message pour lancer l'élection du maire
        self.aff.reinitialiser_screen()
        self.aff.afficher_texte("Il est dorénavant temps d'élire le maire !")
        time.sleep(3)
        self.aff.reinitialiser_screen()

        # Afficher la liste des joueurs encore en vie
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Chaque joueur effectue son vote
        for i in range(0, len(liste)):
            print("\n\n")
            self.aff.afficher_texte(joueurs[i].get_prenom())
            self.aff.phrases("\nPour qui voulez-vous voter ?\n", "WHITE")
            reponse = input()

            # Vérifier que le prénom saisi est valide, sinon redemander
            while reponse not in prenoms:
                self.aff.phrases("Nom pas présent dans la liste, recommencer", "WHITE")
                reponse = input()

            # Ajouter un vote au joueur sélectionné
            for i in range(0, len(joueurs)):
                if joueurs[i].get_prenom() == reponse:
                    joueurs[i].vote()
            self.aff.phrases("Vous avez voté ", "WHITE")

            # Réinitialiser l'écran après chaque vote
            self.aff.reinitialiser_screen()
            self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
            self.aff.liste_joueurs(prenoms, [])

        # Trouver le joueur ayant reçu le maximum de votes
        max = 0
        indice = 0
        for i in range(0, len(joueurs)):
            if max < joueurs[i].get_vote():
                max = joueurs[i].get_vote()
                indice = i

        # Attribuer le rôle de maire au joueur ayant reçu le plus de votes
        joueurs[indice].set_maire(True)

        # Annoncer le capitaine élu
        self.aff.capitaine(joueurs[indice].get_prenom())

        # Réinitialiser les votes de tous les joueurs pour préparer la suite
        for i in range(0, len(joueurs)):
            joueurs[i].reset_vote()

    def afficher_mort_tour(self):
        """
        Objectif : Méthode permettant d'afficher les morts du tour.
        Entrée : Aucune (utilise l'attribut self.mort_tour).
        Sortie : Aucune.
        """
        # Parcourir les joueurs morts ce tour et afficher leur élimination et leur rôle
        for i in self.mort_tour:
            self.aff.eliminer(i)
            self.aff.afficher_texte("Son rôle était : " + i.get_role())
        # Réinitialiser la liste des morts pour le tour suivant
        self.mort_tour = []

    def get_mort_tour(self):
        """
        Objectif : Récupérer la liste des morts du tour.
        Entrée : Aucune.
        Sortie : Liste des morts du tour.
        """
        return self.mort_tour

    def nouveau_maire(self, joueurs, joueur_actuel):
        """
        Objectif : Méthode permettant de choisir un nouveau maire.
        Entrée : joueurs (liste des joueurs) et joueur_actuel (le joueur actuel).
        Sortie : Aucune.
        """
        liste = []
        # Filtrer les joueurs encore en vie pour qu'ils soient éligibles
        for joueur in joueurs:
            if not joueur.get_mort():
                liste.append(joueur)

        prenoms = []
        # Récupérer les prénoms des joueurs encore en vie
        for joueur in liste:
            prenoms.append(joueur.get_prenom())

        # Réinitialiser l'écran et afficher la liste des joueurs éligibles
        self.aff.reinitialiser_screen()
        self.aff.phrases("Liste des joueurs dans la partie : ", "WHITE")
        self.aff.liste_joueurs(prenoms, [])

        # Demander au joueur actuel de choisir le nouveau maire
        self.aff.afficher_texte(joueur.get_prenom())
        self.aff.phrases("Qui voulez-vous choisir comme nouveau maire ?", "WHITE")
        reponse = input().strip()

        # Vérifier que le prénom est valide, sinon redemander
        while reponse not in prenoms:
            self.aff.phrases("Nom pas présent dans la liste, recommencez", "WHITE")
            reponse = input().strip()

        # Attribuer le rôle de maire au joueur sélectionné
        for i in range(len(joueurs)):
            if joueurs[i].get_prenom() == reponse:
                joueurs[i].set_maire(True)

        # Informer que le tour est terminé et réinitialiser l'écran
        self.aff.phrases("Vous avez fini votre tour, appuyer sur entrer pour continuer", "WHITE")
        input()
        joueur_actuel.set_maire(False)
        self.aff.reinitialiser_screen()

    def get_data(self):
        """
        Objectif : Méthode permettant de retourner les données du rôle en format JSON.
        Entrée : Aucune.
        Sortie : res (dictionnaire contenant les données du rôle).
        """
        res = {
            "potion_vie": self.potion_vie,
            "potion_mort": self.potion_mort,
            "lettre_loup_garou": self.lettre_loup_garou,
            "lettre_petite_fille": self.lettre_petite_fille,
            "mort_tour": self.mort_tour,
            "mort": self.mort,
            "loup": self.loup,
            "vote_loup": self.vote_loup
        }
        return res

    def load_data(self, data: dict):
        """
        Objectif : Méthode permettant de charger les données du rôle à partir d'un dictionnaire.
        Entrée : data (dictionnaire contenant les données du rôle).
        Sortie : Aucune.
        """
        # Charger les données de chaque attribut depuis le dictionnaire
        self.potion_vie = data["potion_vie"]
        self.potion_mort = data["potion_mort"]
        self.lettre_loup_garou = data["lettre_loup_garou"]
        self.lettre_petite_fille = data["lettre_petite_fille"]
        self.mort_tour = data["mort_tour"]
        self.mort = data["mort"]
        self.loup = data["loup"]
        self.vote_loup = data["vote_loup"]

