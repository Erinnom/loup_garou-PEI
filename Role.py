import LG_Affichage as affichage
import Joueur
import Partie
import random
class Role():
    def __init__(self):
        self.potion_vie = True
        self.potion_mort = True
    """Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables 
    paramètre : moment
    """
    def sorciere(self,moment):
        if moment == "nuit" :
            if self.potion_vie == True:
                vie = affichage.Affichage()
                vie.sorciere(0,1,"joueur")
                reponse = input()

                while reponse == "oui" or reponse == "non":
                    print("Réponse non accepté")
                    vie.sorciere(0, 1, "joueur")
                    reponse = input()

                if reponse == "oui":
                    self.potion_vie = False

            elif self.potion_mort == True :
                mort = affichage.Affichage()
                mort.sorciere(0,1,"joueur")
                reponse = input()

                while reponse == "oui" or reponse == "non":
                    print("Réponse non accepté")
                    mort.sorciere(0, 1, "joueur")
                    reponse = input()

                if reponse == "oui":
                    self.potion_vie = False

            else :
                pas_potion = affichage.Affichage()
                pas_potion.sorciere(1,0,"joueur")

        else :
            vote = affichage.Affichage()
            vote.vote("joueur")


    """Méthode permettant de créer le rôle voleur avec sa capacité à voler un role au premier tour 
    paramètre : moment
    """
    def voleur(self):

        vol = affichage.Affichage()
        vol.voleur(0,"joueur")
        indice = input("Entrée l'indice du joueur dont vous voulez voler le rôle : ")
        joueurs = Partie.Partie()
        liste = joueurs.get_joueurs()
        nouveau_role = liste[indice].get_role()
        liste[indice].set_role("Villageois")

        for i in liste:
            if liste[i].get_role() == "Voleur":
                liste[i].set_role(nouveau_role)





    """Méthode permettant de créer le rôle villageois 
    paramètre : moment
    """
    def villageois(self,moment, joueur):
        if moment == "nuit":
            villageois = affichage.Affichage()
            villageois.villageois()
        else :
            vote = affichage.Affichage()
            vote.vote(joueur)
    """Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour 
    paramètre : moment
    """
    def voyante(self,moment):
        if moment == "nuit" :
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            voir = affichage.Affichage()
            voir.voyante(0)
            reponse = input()

            while reponse not in liste :
                print("Ce joueur n'existe pas , veuillez renseigner un autre nom")
                reponse = input()

            for i in liste :
                if liste[i].get_joueur() == reponse:
                    resultat = liste[i].get_role()
                    return resultat


        else :
            vote = affichage.Affichage()
            vote.vote()
    """Méthode permettant de créer le rôle loup_garou où il votent la nuit
    paramètre : moment
    """
    def loup_garou(self,moment,joueur):
        pass

    """Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoire des noms des loups-garous
    paramètre : moment
    """
    def petite_fille(self,moment):
        dico = "abcdefhijklmnopqrstuvwxyz"
        if moment == "nuit":
            joueurs = Partie.Partie()
            liste = joueurs.get_joueurs()
            liste_loup =[]
            total_loup = ""
            for i in liste:
                if liste[i].get_role() == "Loup Garou":
                    liste_loup.append(i)
                    total_loup += liste[i].get_joueur()
            for i in range(len(dico)):
                for j in range (len(total_loup)):
                    total_loup[i].lower()
                    if dico[i] == liste_loup[j] :
                        valeur

    """Méthode permettant de créer le rôle chasseur où quand il meurt il tue une personne qu'il choisit
    paramètre : moment
    """
    def chasseur(self,moment,joueur):
        pass

    """Méthode permettant de créer le rôle cupidon où il lie deux personnes et si une des deux meurts alors les deux meurts 
    paramètre : moment
    """
    def cupidon(self,moment,joueur):
        pass

    """Méthode permettant de créer le rôle capitaine où il a vote double 
    paramètre : 
    """
    def capitaine(self,moment,joueur):
        pass