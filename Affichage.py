import Traitement_Image as TI
import os as os
from pyfiglet import Figlet
import random as r


class Affichage:

    def __init__(self):
        pass

    """#####################################################################################################################################################

                                                                        AFFICHAGE IMAGES

    #####################################################################################################################################################"""

    def jour(self):
        """
        Methode qui permettra un affichage d'un fond illustrant la journee et l'arrivee du vote
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/jour.jpg", 70, 60)
        pass

    def nuit(self):
        """
        Methode qui permettra un affichage d'un fond illustrant la nuit et l'arrivee des differents rôles
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/nuit.jpg", 70, 60)
        pass

    def loup_garou(self, temp: bool, nom: str):
        """
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """
        # Phrases pour les loups-garous
        phrases_loups = [
            "Vous avez pose vos griffes sur le cœur de JOUEUR, laissant votre marque indelebile.",
            "Vos crocs se sont refermes sur JOUEUR, et un hurlement silencieux a empli la nuit.",
            "Dans l'ombre, vos instincts predateurs vous ont menes a JOUEUR. Il ne s’y attendait pas.",
            "Une traque habile... JOUEUR est tombe dans le piege que vous lui avez tendu.",
            "Vous avez encercle JOUEUR, vos yeux brillant dans l'obscurite. Il n'avait aucune chance."
        ]
        if temp:
            TI.print_card("./illustration/LG.jpg", 50, 50)
        else:
            TI.print_card("./illustration/griffes.jpg", 40, 40)
            txt = r.choice(phrases_loups)
            avant_joueur, apres_joueur = txt.split("JOUEUR")
            t = avant_joueur + nom + apres_joueur
            self.afficher_texte(t)

        pass

    def sorciere(self, temp: bool, nom: str, choix=None, ):
        """
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise, choix qui donne la potion utilisee
        Return : None
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
            TI.print_card("./illustration/potion.jpg", 40, 40)
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
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
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
            TI.print_card("./illustration/cible.jpg", 40, 40)
            txt = r.choice(phrases_chasseur)
            avant_joueur, apres_joueur = txt.split("JOUEUR")
            t = avant_joueur + nom + apres_joueur
            self.afficher_texte(t)

    def petite_fille(self, temp: bool):
        """
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage
        Return : None
        """
        phrases_petite_fille = [
            "Le regard furtif, vous avez vu les loups rôder dans la nuit. Si vous aviez agi, qui serait encore en vie ?",
            "Un frisson vous traverse en observant les ombres. Vous avez vu, mais n'avez pas ose crier… À quel prix ?",
            "Vos yeux se sont poses sur eux dans la penombre, mais la peur vous a paralysee. Qui etes-vous vraiment, petite fille ?",
            "La nuit etait froide, et pourtant vous avez observe sans bouger, cachee dans l'ombre. Mais avez-vous fait le bon choix ?",
            "Une lueur dans vos yeux… Vous avez vu, vous savez. Mais la tentation de crier ne vous a pas traversee… ou l'avez-vous simplement ignoree ?"
        ]
        if temp:
            TI.print_card("./illustration/Petite-Fille.jpg", 50, 50)
        else:
            TI.print_card("./illustration/ours.jpg", 40, 40)
            t = r.choice(phrases_petite_fille)
            self.afficher_texte(t)

    def voleur(self, temp: bool, nom: str):
        """
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
        """

        # Phrases pour le voleur
        phrases_voleur = [
            "Vos mains tremblantes vont effleure une cartes. Votre choix peut tout changer.",
            "Un sourire satisfait eclaire votre visage tandis que vous glissez la carte choisie dans votre poche.",
            "Devant vous, plusieurs possibilites. Vous avez fait un choix... mais est-il le bon ?",
            "Vos doigts habiles ont choisi avec soin. Votre destin a pris une nouvelle direction.",
            "Une decision audacieuse : vous avez change de rôle, et personne ne le sait encore."
        ]
        if temp:
            TI.print_card("./illustration/Voleur.jpg", 50, 50)
        else:
            TI.print_card("./illustration/pas.jpg", 40, 40)
            t = r.choice(phrases_voleur)
            self.afficher_texte(t)

    def cupidon(self, temp: bool, nom1: str, nom2: str):
        """
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom des joueurs vises
        Return : None
        """
        # Phrases pour Cupidon
        phrases_cupidon = [
            "Vous avez unifie les âmes, JOUEUR. Deux cœurs battent desormais a l'unisson, mais cela peut etre une benediction ou une malediction.",
            "JOUEUR, en tant que Cupidon, vous avez lie deux âmes pour la nuit. Leurs destins sont desormais lies.",
            "JOUEUR, vous avez choisi vos cibles avec soin. L'amour peut etre un puissant allie… ou une arme a double tranchant.",
            "L'amour frappe fort, JOUEUR. Vous avez uni deux joueurs, mais qui seront vos allies et qui seront vos ennemis ?",
            "Cupidon a fait son œuvre, JOUEUR. Le destin des deux amants repose desormais entre vos mains."
        ]

        if temp:
            TI.print_card("./illustration/Cupidon.jpg", 50, 50)
        else:
            TI.print_card("./illustration/coeur.jpg", 50, 40)
            txt = r.choice(phrases_cupidon)
            avant_joueur, milieu_joueur, apres_joueur = txt.split("JOUEUR")
            t = avant_joueur + nom1 + milieu_joueur + nom2 + apres_joueur
            self.afficher_texte(t)

    def voyante(self, temp: bool, nom: str):
        """
        Methode qui permettra un affichage de l'affichage de la carte ou de l'affichage resultant de l'action
        Parameters : booleen qui permet de choisir l'affichage, nom du joueur vise
        Return : None
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
            TI.print_card("./illustration/Voyante.jpg", 50, 50)
        else:
            TI.print_card("./illustration/boule.jpg", 40, 40)
            txt = r.choice(phrases_voyante)
            avant_joueur, apres_joueur = txt.split("JOUEUR")
            t = avant_joueur + nom + apres_joueur
            self.afficher_texte(t)

    def villageois(self):
        """
        Methode qui permettra un affichage de l'affichage de la carte
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/Villageois.jpg", 50, 50)
        pass

    def capitaine(self, nom: str):
        """
        Methode qui permettra un affichage de l'affichage de la carte
        Parameters : None
        Return : None
        """
        # Phrases pour le Capitaine
        phrases_capitaine = [
            "Vous avez pris les renes, JOUEUR. Votre choix determine desormais le destin de l'equipe.",
            "En tant que capitaine, vous guidez le groupe. La decision de JOUEUR pourrait tout changer.",
            "JOUEUR, vous devrez choisir le bon camp. Le sort de tous repose sur vos epaules.",
            "Votre autorite ne fait aucun doute, JOUEUR. Vos choix peuvent sauver ou condamner.",
            "Dans l'ombre de la nuit, vous, JOUEUR, etes la cle de la survie des innocents."
        ]

        TI.print_card("./illustration/Capitaine.jpg", 50, 50)
        txt = r.choice(phrases_capitaine)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)

    def voter(self, nom: str):
        """
        Methode qui permettra un affichage de la seance de vote
        Parameters : None
        Return :
        """
        phrases_votes = [
            "Vous avez vote pour JOUEUR, une voix de plus qui scelle son destin.",
            "Votre voix s'est elevee pour JOUEUR, rapprochant encore la fin de ce villageois.",
            "En votant pour JOUEUR, vous avez contribue a faire pencher la balance contre lui.",
            "Le village connaît votre choix : vous avez vote pour JOUEUR. Une voix de plus vers la fin.",
            "Votre decision a ete claire : vous avez vote pour JOUEUR, une voix qui rapproche la fin de ce villageois.",
            "Avec ce vote pour JOUEUR, vous avez ajoute une voix au jugement du village.",
            "Vous avez pose votre vote sur JOUEUR, une voix supplementaire vers la mort de ce villageois.",
            "Votre vote pour JOUEUR n'a fait qu'approfondir son malheur. La fin est desormais plus proche.",
            "En votant pour JOUEUR, vous avez participe a l'appel de sa condamnation.",
            "Votre choix a ete fait, vous avez vote pour JOUEUR, une voix supplementaire qui pourrait decider de son sort."
        ]

        TI.print_card("./illustration/lettre.jpg", 40, 40)
        txt = r.choice(phrases_votes)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)

    def votes(self, nom: str):
        """
        Methode qui permettra un affichage les votes pour chacun des joueurs
        Parameters : la liste des objets de type joueur
        Return : None
        """
        # Phrases pour Mort au Vote
        phrases_mort_vote = [
            "Le village a parle, JOUEUR. Votre destin a ete scelle par leurs votes.",
            "Vous avez perdu le soutien de vos allies, JOUEUR. Le tribunal a decide.",
            "Les voix du village se sont levees contre vous, JOUEUR. Le verdict est sans appel.",
            "JOUEUR, la decision du village est prise. Vous serez elimine(e) par le vote populaire.",
            "Les villageois ont tranche, JOUEUR. Vous avez ete condamne(e) au bûcher par le vote."
        ]

        TI.print_card("./illustration/lettre-ouverte.jpg", 40, 40)
        txt = r.choice(phrases_mort_vote)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)

    def eliminer(self, nom: str):
        """
        Methode qui permettra un affichage du joueur qui a ete elimine
        Parameters : nom du joueur
        Return : None
        """
        phrases_mort_banale = [
            "La nuit a pris sa vie, et il ne reviendra pas. Le village pleure un autre de ses membres.",
            "Une nouvelle victime du destin cruel. Le village est encore une fois en deuil.",
            "Le silence s'est installe. JOUEUR n'est plus. La quete de survie du village continue.",
            "Les tenebres ont englouti JOUEUR, laissant derriere lui un vide difficile a combler.",
            "Un autre de vos compagnons s'en est alle. Le village est plus faible sans lui.",
            "La mort a frappe a la porte de JOUEUR. Un autre depart qui laisse une trace dans l'âme du village.",
            "La vie de JOUEUR a pris fin dans l'obscurite. Le village devra se remettre de cette perte."
        ]

        TI.print_card("./illustration/faucheuse.jpg", 40, 40)
        txt = r.choice(phrases_mort_banale)
        avant_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom + apres_joueur
        self.afficher_texte(t)

    def morts_amoureux(self, nom1: str, nom2: str):
        """
        Methode qui permettra un affichage des amoureux qui sont morts
        Parameters : nom du joueur1, nom du joueur2
        Return : None
        """
        phrases_mort_amoureux = [
            "La fin tragique de JOUEUR laisse un vide immense, surtout pour celui qu'il aimait. Le cœur du village est brise.",
            "L'amour ne suffit pas a echapper a la mort. JOUEUR et JOUEUR sont maintenant separes a jamais.",
            "Les etoiles s'eteignent pour JOUEUR, et le monde semble plus sombre pour celui qui partageait son amour.",
            "La mort a pris JOUEUR, emportant avec lui un amour aussi profond que la nuit. Leur histoire reste gravee dans les memoires.",
            "C'etait un amour pur, mais meme l'amour ne peut defier la mort. JOUEUR a perdu son bien-aime, et le village perd une lumiere.",
            "Dans la nuit noire, JOUEUR s'en va, laissant son amour devaste. La douleur de cette separation est infinie.",
            "La fin de JOUEUR a emporte avec elle les reves d'un amour qui n'aura jamais de lendemain. Les cœurs brises pleurent cette perte."
        ]

        TI.print_card("./illustration/faucheuse.jpg", 40, 40)
        txt = r.choice(phrases_mort_amoureux)
        avant_joueur, milieu_joueur, apres_joueur = txt.split("JOUEUR")
        t = avant_joueur + nom1 + milieu_joueur + nom2 + apres_joueur
        self.afficher_texte(t)

    def anonyme_screen(self):
        """
        Methode qui permettra un affichage de l'ecran d'attente, pour tous les joueurs a qui ce ne sera pas le tour de jouer
        Parameters : None
        Return : None
        """
        TI.print_card("./illustration/bandeau.jpg", 50, 30)
        pass

    def reinitialiser_screen(self):
        """
        Methode qui permettra d'effacer le terminal
        Parameters : None
        Return : None
        """
        os.system("clear")
        pass

    """#####################################################################################################################################################

                                                                AFFICHAGE TEXTE

    #####################################################################################################################################################"""

    def liste_joueurs(self, liste_joueurs: list, allies: list):
        """
        Methode qui permettra d'afficher la liste des joueurs
        Parameters : Liste des joueurs, lliste des allies
        Return : None
        """
        #copie de la liste des joueurs pour éviter de manipuler la liste original
        l = liste_joueurs.copy()

        #Caracteres pour construire le tableau
        char = ["┌", "┐", "└", "┘", "┴", "┬", "─", "├", "┼", "┤", "│"]

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
            Parameters : None
            Return : None
            """

            print(char[0], end="")
            for _ in range(t):
                for __ in range(max + 4):
                    print(char[6], end="")
                if _ != t - 1:
                    print(char[5], end="")
            print(char[1])
            return

        def ligne_bas(t):
            """
            Fonction qui affiche le contours du tableau (ligne du bas)
            Parameters : None
            Return : None
            """

            print()
            print(char[2], end="")
            for _ in range(t):
                for __ in range(max + 4):
                    print(char[6], end="")
                if _ != t - 1:
                    print(char[4], end="")
            print(char[3])
            return

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

        return

    def phrases(self, text: str, text_color: str, color="WHITE"):
        """
        Methode qui permettra d'afficher du etxte, avec de la couleur sur une partie si voulu
        Parameters : texte, texte a colorer, couleur
        Return : None
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
        return

    def menu_principal(self):
        """
        Methode qui permettra d'afficher le menu d'acceuil du jeu
        Parameters : None
        Return : None
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
        return

    def selection_fichier(self):
        """
        Methode qui permettra d'afficher le menu de chargement d'une partie
        Parameters : None
        Return : None
        """

        self.afficher_texte('Partie', 'big')
        self.afficher_texte('Entrez le nom de votre sauvegarde', 'smbraille')
        return

    def afficher_texte(self, texte: str, font_t='wideterm'):
        """
        Methode qui permettra d'afficher le texte voulu
        Parameters : texte, police du texte
        Return : None
        """
        print()
        f = Figlet(font=font_t)
        print(f.renderText(texte))
        return

    def print_fonts(self):
        """
        Methode qui permettra d'afficher le texte voulu
        Parameters : texte, police du texte
        Return : None
        """

        fonts = [
            "banner",
            "big",
            "block",
            "bubble",
            "circle",
            "digital",
            "emboss",
            "emboss2",
            "future",
            "ivrit",
            "lean",
            "letter",
            "mini",
            "mnemonic",
            "pagga",
            "script",
            "shadow",
            "slant",
            "small",
            "smblock",
            "smbraille",
            "smscript",
            "smshadow",
            "smslant",
            "standard",
            "term",
            "wideterm"]
        for elt in fonts:
            print(elt)
            f = Figlet(font=elt)
            print(f.renderText('Roaer'))
        return


if __name__ == "__main__":
    objet = Affichage()
    objet.menu_principal()
    objet.selection_fichier()
    objet.capitaine('nathan')
    #objet.print_fonts()
