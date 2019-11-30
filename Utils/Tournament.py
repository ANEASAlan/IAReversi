import sys

sys.path.insert(1, '../UI')
sys.path.insert(1, '../Player')

import UI
import myPlayer

# Cette classe permet de stocker un joueur dans un "tournoi"
class PlayerTournament:

    # Initialisation de l'objet (seule fonction, cette classe est en réalité
    # plus proche d'une structure qu'autre chose mais ça n'existe pas en Python)
    def __init__(self, name, heuristic):

        # Le nom du joueur
        self.name = name

        # L'heuristique que le joueur utilise

        # Cette dernière doit avoir pour définition :
        # heuristic(board, move)

        # Les paramètres sont importants car lorsqu'elle est appelée par le
        # joueur, le plateau et le dernier move effectué lui sont passés en
        # paramètres, ne pas avoir cette définition causera donc une erreur lors
        # de l'exécution du code

        # Elle doit renvoyer une valeur dépendant de la couleur
        # Si la valeur témoigne d'un bon coup pour les blancs, la valeur doit
        # être positive, sinon elle doit être négative. Elle est nulle si le
        # coup n'avantage personne
        self.heuristic = heuristic

        # Cette variable permet de compte combien d'autre joueur ce joueur a
        # battu lors du "tournoi"
        self.wins = 0

        # Cette variable permet de compte combien de défaites à subi ce joueur
        # lors du "tournoi"
        self.loses = 0

        # Cette variable permet de compter combien de fois lors du "tournoi"
        # ce joueur a fait match nul
        self.deuces = 0

        # La liste des joueurs que le joueur a battu
        self.won = []

        # La liste des joueurs qui ont battu le ce joueur
        self.lost = []

        # La liste des joueurs contre qui ce joueur a fait match nul
        self.deuced = []

        # Le pourcentage de victoire ce joueur
        self.winRate = 0

    # Cette fonction affiche toutes les données corcernant le joueur actuel
    def printPlayer(self):
        print("----------------------------------\n")
        print("Le joueur " + str(self.name) + " : \n")

        print("A gagné " + str(self.wins) + " fois contre:\n")
        self.printAllPlayers(self.won)
        print("")

        print("A perdu " + str(self.loses) + " fois contre:\n")
        self.printAllPlayers(self.lost)
        print("")

        print("A fait " + str(self.deuces) + " match nul(s) contre:\n")
        self.printAllPlayers(self.deuced)
        print("")

        self.computeWinRate()
        print("Son win rate est de " + str(self.winRate) + "\n")
        print("----------------------------------\n")

    # Cette fonction affiche le nom de tous les joueurs contenus dans le tableau
    # passé en paramère
    def printAllPlayers(self, array):
        for player in array:
            print(player.name)

    # Cette fonction calcul le proportion de victoire de ce joueur
    def computeWinRate(self):
        if self.loses == 0:
            self.winRate = 1
        else:
            self.winRate = self.wins / (self.loses + self.wins + self.deuces)

# Cette classe représente un match
class Match:

    def __init__(self, player1, player2):

        # Le joueur noir
        self.player1 = player1

        # Le joueur blanc
        self.player2 = player2

        # Le gagnant
        self.winner = None

        # Le perdant
        self.loser = None

    def getBlack(self):
        return self.player1

    def getWhite(self):
        return self.player2

# Cette classe représente un tournoi dans lequel cahque joueur s'affronte deux
# fois
class Tournament:

    def __init__(self):

        # La liste des matchs qui devront être joués
        self.matchs = []

    # Permet d'ajouter un match à la liste des matchs
    def addMatch(self, match):
        if not match in self.match:
            self.match.append(match)

    # Permet d'ajouter un match à la liste des matchs
    def addMatch(self, player1, player2):
        match = Match(player1, player2)
        if not match in self.matchs:
            self.matchs.append(match)

    def createAllMatchs(self, players):
        # On parcourt la liste des joueurs et on crée un match entre eux
        # Cela permet de créer deux matchs par couple de joueurs, en inversant
        # leur couleur
        for player1 in players:
            for player2 in players:

                # On ajoute pas le match qui fait s'opposer un joueur à lui-même
                if player1 != player2:
                    self.addMatch(player1, player2)

    def startTournament(self, boardSize, withUI):
        # On va traverser les joueurs pour qu'ils s'affrontent, d'abord noir v blanc
        # puis blanc v noir
        for match in self.matchs:

            # On crée le plateau de jeu avec une taille de 10
            board = UI.createBoard(boardSize)

            # On récupère le résultat du match pour changer les stats des joueurs
            res = startMatch(board, match, boardSize, withUI)

            # On récupère le résultat
            res = UI.printWinner(board, res)

            # On change les stats des joueurs
            self.updateStats(match, res)

    # Cette fonction change les stats des joueurs du match
    def updateStats(self, match, res):

        # On récupère le joueur blanc et le joueur noir afin d'alléger la
        # suite du code
        black = match.getBlack()
        white = match.getWhite()

        # Si les blancs ont gagné
        if res == 0:
            self.modifyPlayers(white, black)
            match.winner = white
            match.loser = black

        # Si les noirs ont gagné
        elif res == 1:
            self.modifyPlayers(black, white)
            match.winner = black
            match.loser = white

        # Si il y a eu égalité
        else:
            white.deuces += 1
            black.deuces += 1
            white.deuced.append(black)
            black.deuced.append(white)

    # Cette fonction modifie les stats en fonction du gagnant et du perdant
    def modifyPlayers(self, winner, loser):

        # Le gagnant a gagné une fois de plus, le perdant a perdu une fois de
        # plus
        winner.wins += 1
        loser.loses += 1

        # Si le perdant n'est pas encore dans la liste des joueurs battus par
        # le gagnant, on l'y ajoute
        if not loser in winner.won:
            winner.won.append(loser)

        # Si le gagnant n'est pas encore dans la liste des joueurs ont battu
        # le perdant, on l'y ajoute
        if not winner in loser.lost:
            loser.lost.append(winner)

# Cette fonction démarre un match donné en paramètre sur un plateau de taille
# donnée
def startMatch(board, match, boardSize, withUI):

    # On récupère le joueur blanc et le joueur noir afin d'alléger la
    # suite du code
    black = match.getBlack()
    white = match.getWhite()

    # On affiche le nom de chaque joueur
    print("Noir : " + str(black.name))
    print("Blanc : " + str(white.name))

    # On crée nos deux joueurs avec les bonnes heuristiques
    # On leur laisse 5 secondes pour décider chaque coup

    player1 = myPlayer.myPlayer(black.heuristic, 5, boardSize)
    player2 = myPlayer.myPlayer(white.heuristic, 5, boardSize)

    # On donne au plyer1 les noirs et au player2 les blancs
    competitors = UI.assignColors(board, player1, player2)

    # On démarre le match
    return UI.play(board, competitors, withUI)
