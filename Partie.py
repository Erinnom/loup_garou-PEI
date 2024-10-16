class Partie():
    def __init__(self):
        self.id_partie = ""         #Nom de la partie qui permet de l'identifier
        self.nombre_joueur = 0      #Nombre de joueurs qui joue à cette partie
        self.etat_partie = 0        #Information qui détermines à quel endroit du tour la partie en est


    def creer(self, id_partie : str, nbr_joueur : int):
        """Méthode permettant de créer une nouvelle partie en spécifiant
            son identifiant et permettant la saisie des joueurs et leur attribution
             des rôles"""
        pass

    def sauvegarder(self, nom_fichier: str):
        """Méthode permettant de sauvegarder la partie en cours
            dans un document Json"""
        pass

    def charger(self, id_partie: str):
        """Méthode permettant de charger un fichier Json pour
            reprendre la partie là où elle c'est arrêté"""
        pass

    def tour(self):
        """Méthode qui effectue tout un tour de jeu"""
        pass

    def get_id(self):
        return self.id_partie

    def get_nombre_joueur(self):
        return self.nombre_joueur

    def get_etat(self):
        return self.etat_partie



if __name__ == "__main__":
    test = Partie()
    test.creer("Partie_test",4)
    print(test.id_partie)