import pyfiglet

import Traitement_Image as TI
import os
import time
from pyfiglet import *
import random as r


class Affichage:

    """#####################################################################################################################################################

                                                                        AFFICHAGE IMAGES

    #####################################################################################################################################################"""

    def jour(self):
        """
        Objectif : Méthode qui permettra un affichage d'un fond illustrant la journee et l'arrivee du vote
        Entrée : Aucune
        Sortie : Aucune
        """
        self.reinitialiser_screen()
        TI.print_card("./illustration/jour.jpg", 50, 50)
        time.sleep(2)
        self.reinitialiser_screen()
        self.afficher_texte("La nuit est terminée, le village se reveille...")
        time.sleep(5)
        self.reinitialiser_screen()

    def nuit(self):
        """
        Objectif : Méthode qui permettra un affichage d'un fond illustrant la nuit et l'arrivee des differents rôles
        Entrrée : Aucune
        Sortie : Aucune
        """
        self.reinitialiser_screen()
        TI.print_card("./illustration/nuit.jpg", 50, 50)
        time.sleep(2)
        self.reinitialiser_screen()
        self.afficher_texte("La nuit tombe sur le village de Thiercelieux... Le Village s'endort...")
        time.sleep(5)
        self.reinitialiser_screen()

    def loup_garou(self, temp: bool, nom: str):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Entrée : booleen qui permet de choisir l'affichage, nom du joueur vise
        Sortie : Aucune
        """
        # Phrases pour les loups-garous
        phrases_loups = [
            "Vous avez pose vos griffes sur le coeur de JOUEUR, laissant votre marque indelebile.",
            "Vos crocs se sont refermes sur JOUEUR, et un hurlement silencieux a empli la nuit.",
            "Dans l'ombre, vos instincts predateurs vous ont menes a JOUEUR. Il ne s’y attendait pas.",
            "Une traque habile... JOUEUR est tombe dans le piege que vous lui avez tendu.",
            "Vous avez encercle JOUEUR, vos yeux brillant dans l'obscurite. Il n'avait aucune chance."
        ]
        if temp:
            TI.print_card("./illustration/LG.jpg", 50, 50)
        else:
            self.reinitialiser_screen()
            TI.print_card("./illustration/griffes.jpg", 40, 40)
            time.sleep(3)
            self.reinitialiser_screen()
            txt = r.choice(phrases_loups)
            avant_joueur, apres_joueur = txt.split("JOUEUR")
            texte_final = avant_joueur + nom + apres_joueur
            self.afficher_texte(texte_final)

    def sorciere(self, temp: bool, nom: str, choix=None, ):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Entrée : booleen qui permet de choisir l'affichage, nom du joueur vise
        Sortie : Aucune
        """
        # Phrases pour la sorciere
        phrases_potion_vie = [
            "Avec un geste rapide, vous versez la potion de vie sur JOUEUR. Un souffle de vie se reveille en lui. Il est sauve, mais vous aurez a repondre de vos choix.",
            "La potion de vie brille dans vos mains, et vous la versez sur JOUEUR. Une lueur verte illumine son visage. Il respire a nouveau.",
            "Vous murmurez les mots d'un ancien sortilege et versez la potion sur JOUEUR. Un frisson traverse son corps, mais la vie reprend peu a peu.",
            "Dans un dernier souffle, vous brisez la fiole contenant la potion de vie et la deposez sur JOUEUR. Un fremissement de vie le traverse.",
            "Le liquide scintillant touche les levres de JOUEUR. Vous avez choisi de lui offrir une chance. Il est desormais sauve, a vous de voir si ce choix etait le bon.",
            "La potion de vie eclaire votre visage, et en un geste, vous l'offrez a JOUEUR. Il se reveille, redonnant un souffle de vie a ses poumons.",
            "Vous faites un dernier mouvement magique, et la potion de vie s'ecoule sur JOUEUR. La magie opere, sa vie est maintenant entre vos mains."
        ]

        phrases_potion_mort = [
            "Avec une lueur malfaisante, vous brisez la fiole de potion de mort sur JOUEUR. Un cri etouffe s'echappe de sa gorge avant qu'il ne tombe dans un silence eternel.",
            "Dans l'obscurite de la nuit, vous versez la potion de mort sur JOUEUR. Un dernier souffle, et il est emporte par la nuit, sans espoir de retour.",
            "La magie noire se fait sentir, et la potion de mort penetre les veines de JOUEUR. Il lutte, mais la fin est inevitable. Il s'effondre, sans vie.",
            "Vous versez la potion sur JOUEUR, et en un instant, sa vie s'echappe de lui. Vous avez choisi la voie de la mort. Un autre joueur tombe.",
            "La potion de mort fait son effet instantanement. JOUEUR est submerge par la noirceur. Vous sentez son energie s'echapper dans l'air froid.",
            "Le poison de la potion de mort envahit rapidement le corps de JOUEUR. Il n'a pas le temps de resister et tombe dans l'obscurite de la nuit.",
            "Avec un geste decide, vous liberez la potion de mort sur JOUEUR. Un dernier tremblement, et tout est fini. Il a rejoint les ombres."
        ]

        if temp:
            TI.print_card("./illustration/Sorciere.jpg", 50, 50)
        else:
            self.reinitialiser_screen()
            TI.print_card("./illustration/potion.jpg", 40, 40)
            time.sleep(3)
            self.reinitialiser_screen()
            if choix == "vie":
                txt = r.choice(phrases_potion_vie)
                avant_joueur, apres_joueur = txt.split("JOUEUR")
                t = avant_joueur + nom + apres_joueur
                self.afficher_texte(t)
            elif choix == "mort":
                txt = r.choice(phrases_potion_mort)
                avant_joueur, apres_joueur = txt.split("JOUEUR")
                t = avant_joueur + nom + apres_joueur
                self.afficher_texte(t)

    def chasseur(self, temp: bool, nom: str):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Entrée : booleen qui permet de choisir l'affichage, nom du joueur vise
        Sortie : Aucune
        """
        phrases_chasseur = [
            "Vous avez tire sur JOUEUR, cela lui aura ete fatal. Le destin du village est desormais scelle.",
            "Le coup de feu a resonne. JOUEUR est tombe, et avec lui, une partie de l'espoir du village.",
            "Votre tir a fauche JOUEUR. La decision est prise, et l'issue est irreversible.",
            "Dans un ultime acte, vous avez abattu JOUEUR. Que le village vous pardonne ou vous juge.",
            "Le tir a frappe juste. JOUEUR est desormais hors du jeu. Le poids de cette decision pese lourd.",
            "JOUEUR n'a pas eu le temps de reagir. Le tir est parti, et maintenant il ne reste que des regrets.",
            "Votre arme a fait son œuvre, et JOUEUR n'est plus. Le village devra vivre avec cette decision."
        ]

        if temp:
            TI.print_card("./illustration/Chasseur.jpg", 50, 50)
        else:
            self.reinitialiser_screen()
            TI.print_card("./illustration/cible.jpg", 40, 40)
            time.sleep(3)
            self.reinitialiser_screen()
            txt = r.choice(phrases_chasseur)
            avant_joueur, apres_joueur = txt.split("JOUEUR")
            t = avant_joueur + nom + apres_joueur
            self.afficher_texte(t)

    def petite_fille(self, temp: bool):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Entrée : booleen qui permet de choisir l'affichage
        Sortie : Aucune
        """
        phrases_petite_fille = [
            "Le regard furtif, vous avez vu les loups rôder dans la nuit. Si vous aviez agi, qui serait encore en vie ?",
            "Un frisson vous traverse en observant les ombres. Vous avez vu, mais n'avez pas ose crier... A quel prix ?",
            "Vos yeux se sont poses sur eux dans la penombre, mais la peur vous a paralysee. Qui etes-vous vraiment, petite fille ?",
            "La nuit etait froide, et pourtant vous avez observe sans bouger, cachee dans l'ombre. Mais avez-vous fait le bon choix ?",
            "Une lueur dans vos yeux... Vous avez vu, vous savez. Mais la tentation de crier ne vous a pas traversee... ou l'avez-vous simplement ignoree ?"
        ]
        if temp:
            TI.print_card("./illustration/Petite-Fille.jpg", 50, 50)
        else:
            self.reinitialiser_screen()
            TI.print_card("./illustration/ours.jpg", 40, 40)
            time.sleep(3)
            self.reinitialiser_screen()
            t = r.choice(phrases_petite_fille)
            self.afficher_texte(t)

    def voleur(self, temp: bool):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Entrée : booleen qui permet de choisir l'affichage, nom du joueur vise
        Sortie : Aucune
        """

        # Phrases pour le voleur
        phrases_voleur = [
            "Vos mains tremblantes vont effleure une cartes. Votre choix peut tout changer.",
            "Un sourire satisfait eclaire votre visage tandis que vous glissez la carte choisie dans votre poche.",
            "Devant vous, plusieurs possibilites. Vous avez fait un choix... mais est-il le bon ?",
            "Vos doigts habiles ont choisi avec soin. Votre destin a pris une nouvelle direction.",
            "Une decision audacieuse : vous avez change de role, et personne ne le sait encore."
        ]
        if temp:
            TI.print_card("./illustration/Voleur.jpg", 50, 50)
        else:
            self.reinitialiser_screen()
            TI.print_card("./illustration/pas.jpg", 40, 40)
            time.sleep(3)
            self.reinitialiser_screen()
            t = r.choice(phrases_voleur)
            self.afficher_texte(t)
            time.sleep(4)
            self.reinitialiser_screen()

    def cupidon(self, temp: bool, nom1: str, nom2: str):
        """
        Objectif : Méthode qui permettra un affichage de la carte ou de l'affichage résultant de l'action.
        Entrée : booléen qui permet de choisir l'affichage, noms des joueurs visés.
        Sortie : Aucune.
        """
        # Phrases pour Cupidon
        phrases_cupidon = [
            "JOUEUR1 et JOUEUR2 sont maintenant unis par le destin.",
            "JOUEUR1 et JOUEUR2, leurs vies sont liees pour le meilleur ou pour le pire.",
            "L'amour frappe JOUEUR1 et JOUEUR2. Seront-ils allies ou ennemis ?",
            "JOUEUR1 et JOUEUR2, deux coeurs battent a l'unisson.",
            "Cupidon a choisi JOUEUR1 et JOUEUR2. Leur destin est scelle."
        ]

        if temp:
            TI.print_card("./illustration/Cupidon.jpg", 50, 50)
        else:
            self.reinitialiser_screen()
            TI.print_card("./illustration/coeur.jpg", 50, 40)
            time.sleep(3)
            self.reinitialiser_screen()

            # Choisir une phrase aléatoire et remplacer JOUEUR1 et JOUEUR2
            txt = r.choice(phrases_cupidon)
            texte_final = txt.replace("JOUEUR1", nom1).replace("JOUEUR2", nom2)

            self.afficher_texte(texte_final)

    def voyante(self, temp: bool, nom: str):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Entrée : booleen qui permet de choisir l'affichage, nom du joueur vise
        Sortie : Aucune
        """
        # Phrases pour la voyante
        phrases_voyante = [
            "Dans vos visions, JOUEUR se devoile... Un allie ? Un ennemi ? Le mystere s’epaissit.",
            "La verite se devoile sous vos yeux. JOUEUR est-il vraiment celui qu’il pretend etre ?",
            "Vos pouvoirs ont perce le voile... JOUEUR a ete mis a nu par vos visions.",
            "Une lumiere etrange eclaire JOUEUR. Ses intentions deviennent claires pour vous seul(e).",
            "En plongeant dans les ombres, vous avez decouvert ce que JOUEUR cache au fond de lui."
        ]

        if temp:
            self.reinitialiser_screen()
            TI.print_card("./illustration/boule.jpg", 40, 40)
            time.sleep(3)
        else:
            self.reinitialiser_screen()
            txt = r.choice(phrases_voyante)
            avant_joueur, apres_joueur = txt.split("JOUEUR")
            t = avant_joueur + nom + apres_joueur
            self.afficher_texte(t)


    def capitaine(self, nom: str):
        """
        Objectif : Méthode qui permettra un affichage de l'affichage de la carte
        Entrée : Aucune
        Sortie : Aucune
        """
        # Phrases pour le Capitaine
        phrases_capitaine = [
            "Vous avez pris les renes, JOUEUR. Votre choix determine desormais le destin de l'equipe.",
            "En tant que capitaine, vous guidez le groupe. La decision de JOUEUR pourrait tout changer.",
            "JOUEUR, vous devrez choisir le bon camp. Le sort de tous repose sur vos epaules.",
            "Votre autorite ne fait aucun doute, JOUEUR. Vos choix peuvent sauver ou condamner.",
            "Dans l'ombre de la nuit, vous, JOUEUR, etes la cle de la survie des innocents."
        ]

        self.reinitialiser_screen()
        TI.print_card("./illustration/Capitaine.jpg", 50, 50)
        time.sleep(3)
        self.reinitialiser_screen()
        txt = r.choice(phrases_capitaine)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)
        time.sleep(6)

    def voter(self, nom: str):
        """
        Objectif : Méthode qui permettra un affichage de la seance de vote
        Entrée : Aucune
        Sortie : Aucune
        """
        phrases_votes = [
            "Vous avez vote pour JOUEUR, une voix de plus qui scelle son destin.",
            "Votre voix s'est elevee pour JOUEUR, rapprochant encore la fin de ce villageois.",
            "En votant pour JOUEUR, vous avez contribue a faire pencher la balance contre lui.",
            "Le village connait votre choix : vous avez vote pour JOUEUR. Une voix de plus vers la fin.",
            "Votre decision a ete claire : vous avez vote pour JOUEUR, une voix qui rapproche la fin de ce villageois.",
            "Avec ce vote pour JOUEUR, vous avez ajoute une voix au jugement du village.",
            "Vous avez pose votre vote sur JOUEUR, une voix supplementaire vers la mort de ce villageois.",
            "Votre vote pour JOUEUR n'a fait qu'approfondir son malheur. La fin est desormais plus proche.",
            "En votant pour JOUEUR, vous avez participe a l'appel de sa condamnation.",
            "Votre choix a ete fait, vous avez vote pour JOUEUR, une voix supplementaire qui pourrait decider de son sort."
        ]

        self.reinitialiser_screen()
        TI.print_card("./illustration/lettre.jpg", 40, 40)
        time.sleep(1)
        self.reinitialiser_screen()
        txt = r.choice(phrases_votes)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)
        time.sleep(3)

    def votes(self, nom: str, role:str):
        """
        Objectif : Méthode qui permettra un affichage les votes pour chacun des joueurs
        Entrée : la liste des objets de type joueur
        Sortie : Aucune
        """
        # Phrases pour Mort au Vote
        phrases_mort_vote = [
            "Le village a parle, JOUEUR. Votre destin a ete scelle par leurs votes.",
            "Vous avez perdu le soutien de vos allies, JOUEUR. Le tribunal a decide.",
            "Les voix du village se sont levees contre vous, JOUEUR. Le verdict est sans appel.",
            "JOUEUR, la decision du village est prise. Vous serez elimine(e) par le vote populaire.",
            "Les villageois ont tranche, JOUEUR. Vous avez ete condamne(e) au bucher par le vote."
        ]

        self.reinitialiser_screen()
        TI.print_card("./illustration/lettre-ouverte.jpg", 40, 40)
        time.sleep(3)
        self.reinitialiser_screen()
        txt = r.choice(phrases_mort_vote)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)
        time.sleep(6)
        self.reinitialiser_screen()
        self.afficher_texte("Vous etiez : "+ role)
        time.sleep(4)

    def eliminer(self, nom: str):
        """
        Objectif : Méthode qui permettra un affichage du joueur qui a été éliminé.
        Entrée : nom du joueur
        Sortie : Aucune
        """
        phrases_mort_banale = [
            "La nuit a pris la vie de JOUEUR, et il ne reviendra pas. Le village pleure un autre de ses membres.",
            "Une nouvelle victime du destin cruel. JOUEUR rejoint les rangs des disparus, et le village est encore une fois en deuil.",
            "Le silence s'est installe. JOUEUR n'est plus. La quete de survie du village continue sans lui.",
            "Les tenebres ont englouti JOUEUR, laissant derriere lui un vide difficile a combler pour le village.",
            "Un autre de vos compagnons s'en est alle, et JOUEUR n'est plus parmi nous. Le village est plus faible sans lui.",
            "La mort a frappe a la porte de JOUEUR. Un autre depart qui laisse une trace dans l'ame du village.",
            "La vie de JOUEUR a pris fin dans l'obscurite. Le village devra se remettre de cette perte immense."
        ]

        self.reinitialiser_screen()
        TI.print_card("./illustration/faucheuse.jpg", 40, 40)
        time.sleep(3)
        self.reinitialiser_screen()

        # Choisir une phrase et remplacer JOUEUR par le nom
        txt = r.choice(phrases_mort_banale)
        t = txt.replace("JOUEUR", nom)
        self.afficher_texte(t)
        time.sleep(6)

    def morts_amoureux(self, nom1: str, nom2: str):
        """
        Objectif Methode qui permettra un affichage des amoureux qui sont morts
        Entrée : nom du joueur1, nom du joueur2
        Return : None
        """
        phrases_mort_amoureux = [
            "La fin tragique de JOUEUR laisse un vide immense, surtout pour celui qu'il aimait. Le coeur du village est brise.",
            "L'amour ne suffit pas a echapper a la mort. JOUEUR et JOUEUR sont maintenant separes a jamais.",
            "Les etoiles s'eteignent pour JOUEUR, et le monde semble plus sombre pour celui qui partageait son amour.",
            "La mort a pris JOUEUR, emportant avec lui un amour aussi profond que la nuit. Leur histoire reste gravee dans les memoires.",
            "C'etait un amour pur, mais meme l'amour ne peut defier la mort. JOUEUR a perdu son bien-aime, et le village perd une lumiere.",
            "Dans la nuit noire, JOUEUR s'en va, laissant son amour devaste. La douleur de cette separation est infinie.",
            "La fin de JOUEUR a emporte avec elle les reves d'un amour qui n'aura jamais de lendemain. Les coeurs brises pleurent cette perte."
        ]

        self.reinitialiser_screen()
        TI.print_card("./illustration/faucheuse.jpg", 40, 40)
        time.sleep(3)
        self.reinitialiser_screen()
        txt = r.choice(phrases_mort_amoureux)
        avant_joueur, milieu_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom1 + milieu_joueur + nom2 + apres_joueur
        self.afficher_texte(t)

    def anonyme_screen(self):
        """
        Objectif : Méthode qui permettra un affichage de l'écran d'attente, pour tous les joueurs à qui ce ne sera pas le tour de jouer
        Entrée : Aucune
        Sortie : Aucune
        """
        TI.print_card("./illustration/bandeau.jpg", 50, 30)

    def reinitialiser_screen(self):
        """
        Objectif : Méthode qui permettra d'effacer le terminal
        Entrée : Aucune
        Sortie : Aucune
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    """#####################################################################################################################################################

                                                                AFFICHAGE TEXTE

    #####################################################################################################################################################"""

    def liste_joueurs(self,  listes_joueurs : list, allies : list):
        """
        Objectif : Méthode qui permettra d'afficher la liste des joueurs
        Entrée : Liste des joueurs, lliste des alliés
        Sortie : Aucune
        """
        #copie de liste pour éviter les manipulations sur liste d'origine
        l = listes_joueurs.copy()


        #Caractères pour construire le tableau
        char = ["┌", "┐", "└", "┘", "┴", "┬","─", "├", "┼", "┤", "│"]

        #Couleurs pour differencier allies et ennemis
        RED = "\033[31m"
        GREEN = "\033[32m"
        BLUE = "\033[34m"
        RESET = "\033[0m"

        length = len(l)
        max = 0

        for j in l:
            if len(j) > max:
                max = len(j)

        def ligne_haut(t):
            """
            Fonction qui affiche le contours du tableau (ligne du haut)
            Parameters : Aucune
            Sortie : Aucune
            """
            print(char[0], end = "")
            for _ in range(t):
                for __ in range (max+4):
                    print(char[6], end ="")
                if _ != t-1:
                    print(char[5], end = "")
            print(char[1])

        def ligne_bas(t):
            """
            Objectif : Fonction qui affiche le contours du tableau (ligne du bas)
            Entrée : Parameters : None
            Sortie : None
            """

            print()
            print(char[2], end="")
            for _ in range(t):
                for __ in range(max + 4):
                    print(char[6], end="")
                if _ != t - 1:
                    print(char[4], end="")
            print(char[3])

        ligne_supp = 0
        if len(l) < 10:
            t = len(l)
        else:
            t = 10
        if length % 10 != 0:
            ligne_supp += 1

        #Affichage des prenoms dans le tableau

        for joueur in range(length // 10 + ligne_supp):
            ligne_haut(t)
            print(char[-1], end="")
            for _ in range(10):
                if l == []:
                    for __ in range(max + 4):
                        print(" ", end="")
                else:
                    nom = l.pop(0)
                    ecart = max - len(nom)
                    for __ in range(ecart // 2 + 2):
                        print(" ", end="")
                    if nom in allies:
                        print(f"{RED}{nom}{RESET}", end="")

                    else:
                        print(f"{GREEN}{nom}{RESET}", end="")
                    for __ in range(ecart // 2 + ecart % 2 + 2):
                        print(" ", end="")
                    print(char[-1], end="")

            ligne_bas(t)



    def phrases(self, text : str, text_color : str,  color = "WHITE"):
        """
        Objectif : Méthode qui permettra d'afficher du etxte, avec de la couleur sur une partie si voulu
        Parameters : texte, texte à colorer, couleur
        Sortie : Aucune
        """
        COLORS = {
            "BLACK": "\033[30m",
            "RED": "\033[31m",
            "GREEN": "\033[32m",
            "YELLOW": "\033[33m",
            "BLUE": "\033[34m",
            "MAGENTA": "\033[35m",
            "CYAN": "\033[36m",
            "PINK": "\033[38;5;205m",
            "WHITE": "\033[37m",
        }
        RESET = "\033[0m"
        DEFAUT = "WHITE"
        color = color.upper()
        if color not in COLORS:
            color = "WHITE"
        if text_color != "":
            avant, milieu, apres = text.partition(text_color)
            print(f"{COLORS[DEFAUT]}{avant}{RESET}", end="")
            print(f"{COLORS[color]}{milieu}{RESET}", end="")
            print(f"{COLORS[DEFAUT]}{apres}{RESET}")
        else:
            print(f"{COLORS[DEFAUT]}{text}{RESET}")



    def menu_principal(self):
        """
        Objectif : Méthode qui permettra d'afficher le menu d'acceuil du jeu
        Parameters : Aucune
        Sortie : Aucune
        """
        self.afficher_texte('Loup - Garou', 'big')
        print("\n \t🄼 🄰 🄳 🄴  🄱 🅈  🄼 🄴 🄰 🄼  🅃 🄴 🄰 🄼\n")
        options = [
            "ℂ𝕣𝕖́𝕖𝕣 𝕦𝕟𝕖 𝕡𝕒𝕣𝕥𝕚𝕖 - 𝟙",
            "ℂ𝕙𝕒𝕣𝕘𝕖𝕣 𝕦𝕟𝕖 𝕡𝕒𝕣𝕥𝕚𝕖 - 𝟚",
            "ℚ𝕦𝕚𝕥𝕥𝕖𝕣 𝕝𝕖 𝕛𝕖𝕦 - 𝟛"

        ]
        for o in options:
            print()
            print("\t\t", o)

        print("\n\n")

    def afficher_texte(self, texte: str, font_t='dos_rebel'):
        """
        Objectif : Methode qui permettra d'afficher le texte voulu
        Entrée : texte, police du texte
        Sortie : None
        """
        f = Figlet(font=font_t, width=200)
        print(f.renderText(texte))

    def print_fonts(self):
        """
        Objectif : Methode qui permettra d'afficher le texte voulu
        Entrée : texte, police du texte
        Sortie : None
        """

        fonts = pyfiglet.FigletFont.getFonts()

        for elt in fonts:
            print(elt)
            f = Figlet(font=elt)
            print(f.renderText('Ceci est un test'))

    def print_cards(self, chemin):
        TI.print_card(chemin, 50, 50)


if __name__ == "__main__":
    test = Affichage()
    test.print_fonts()
    input()
