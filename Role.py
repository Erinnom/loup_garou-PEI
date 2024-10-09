import LG_Affichage as affichage
class Role():
    def __init__(self,role):
        self.role = role

    """Méthode permettant de créer le rôle sorcière avec ses deux potions utilisables 
    paramètre : moment
    """
    def sorciere(self,moment,potion_vie,potion_mort,joueur):
        if moment == "nuit" :
            if potion_vie == True:
                vie = affichage.Affichage()
                vie.sorciere(0,"vie",joueur)
            elif potion_mort == True :
                mort = affichage.Affichage()
                mort.sorciere(0,"mort",joueur)
            else :
                pas_potion = affichage.Affichage()
                pas_potion.sorciere(0,"pas_potion",joueur)
        else :
            vote = affichage.Affichage()
            vote.vote(joueur)

    """Méthode permettant de créer le rôle voleur avec sa capacité à voler un role au premier tour 
    paramètre : moment
    """
    def voleur(self):
        pass

    """Méthode permettant de créer le rôle villageois 
    paramètre : moment
    """
    def villageois(self):
        pass

    """Méthode permettant de créer le rôle voyante avec sa capacité à voir un role d'une personne chaque tour 
    paramètre : moment
    """
    def voyante(self):
        pass

    """Méthode permettant de créer le rôle loup_garou où il votent la nuit
    paramètre : moment
    """
    def loup_garou(self):
        pass

    """Méthode permettant de créer le rôle petite_fille où elle obtient des lettres aléatoire des noms des loups-garous
    paramètre : moment
    """
    def petite_fille(self):
        pass

    """Méthode permettant de créer le rôle chasseur où quand il meurt il tue une personne qu'il choisit
    paramètre : moment
    """
    def chasseur(self):
        pass

    """Méthode permettant de créer le rôle cupidon où il lie deux personnes et si une des deux meurts alors les deux meurts 
    paramètre : moment
    """
    def cupidon(self):
        pass

    """Méthode permettant de créer le rôle capitaine où il a vote double 
    paramètre : 
    """
    def capitaine(self):
        pass