class Partie():
    def __init__(self):
        self.id_partie = ""
        self.nombre_joueur = 0


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

if __name__ == "__main__":
    test = Partie("Partie_test")
    help(Partie.creer)