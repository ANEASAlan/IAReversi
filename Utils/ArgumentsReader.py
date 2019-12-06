# Cette classe représente la liste des arguments possibles
class Argument:

    def __init__(self):

        # Est-ce que l'utilisateurr a demandé une fenere graphique
        self.withUI = False

        # La taille du plateau
        self.boardSize = 10

        # Combien de tounoi il faut effectuer
        self.nbTournament = 0

        # La liste des matchs que l'utilisateur demande
        self.matchs = []

        # Est-ce qu'on affiche tous les joueurs possibles
        self.displayPlayers = False

        # Le temps maximum autorisés à passer dans l'arbre des coups
        self.maxTime = 5

        # Le fichier dans lequel sauvegarder les résultats du tournoi, si il
        # y en a un
        self.filename = "Data/Results.xlsx"

    # Cette fonction affiche tous les arguments et leur valeur
    def printArgs(self):
        print("----------------------")
        if self.withUI:
            print("UI is ON")
        else:
            print("UI is OFF")
        print("Board size is " + str(self.boardSize))
        if self.nbTournament:
            print("There will be " + str(self.nbTournament) + " tournament")
        else:
            print("There won't be any tournaments")
        print("")
        if self.matchs:
            print("Planned matchs:")
            for match in self.matchs:
                print(match[0] + " vs " + match[1])
        print("----------------------")
        print("")

# Cette fonction lit les arguments passés en paramètre et retourne un objet
# de type Argument
def getArguments(argv):

    # La liste des arguemnts à prendre en compte
    arguments = Argument()

    # On parcourt tous les arguments contenus dans argv
    # Index est l'index de l'argument que nous sommes en train de lire
    # Cette variable permet d'ensuite récupèrer les possibles arguments liés
    # à celui qui est en train d'être lu
    for index in range(len(argv)):

        # Si l'agument est -UI
        if "-UI" == argv[index]:
            arguments.withUI = True

        # Si l'argument est -BDS (boardsize)
        if "-BDS" == argv[index]:

            # On récupère l'argument suivant
            # On a besoin d'un try/catch pou s'assurer que la valeur suivante
            # est un entier
            try:
                size = int(argv[index + 1])
                if size <= 4 or size % 2 == 1:
                    print("Error: Board size is invalid. Defaults to 10")
                else:
                    arguments.boardSize = size
            except Exception as e:
                print("Error: Board Size is invalid. Defaults to 10")

        # Si l'argument est -T
        if "-T" == argv[index]:

            arguments.nbTournament = 1
            # On récupère l'argument suivant pour savoir combien de tournoi
            # il faut effectuer, si la valeur est invalide, un seul tournoi sera
            # effectué
            try:
                nb = int(argv[index + 1])
                if nb <= 0:
                    print("Error: Invalid number of tournaments. Defaults to 1")
                else:
                    arguments.nbTournament = nb
            except Exception as e:
                pass

        # Si l'argument est -M
        if "-M" == argv[index]:

            # La deux joueurs paticipant au match (si ils n'existent pas
            # le match n'aura pas lieu)
            # Si c'est la fin des arguments, on n'ajoute pas de match
            # car au moins un des eux joueurs n'a pas été donné
            if index + 2 < len(argv):
                player1 = argv[index + 1]
                player2 = argv[index + 2]
                arguments.matchs.append([player1, player2])

        # Si l'argument est -h
        if "-h" == argv[index]:
            printHelp()

        # Si l'argument est -P
        if "-P" == argv[index]:
            arguments.displayPlayers = True

        # Si l'argument est -TM
        if "-TM" == argv[index]:

            # On récupère l'argument suivant, censé être le temps maximal
            # autorisé pour chercher dans le meilleur coup
            # On a encore une fois besoin d'un bloc try/catch dans le cas
            # où l'argument suivant n'est pas un nombre
            try:
                time = float(argv[index + 1])
                if time <= 0:
                    print("Error: Invalid time. Defaults to 5 seconds")
                else:
                    arguments.maxTime = time
            except Exception as e:
                print("Error: Invalid time. Defaults to 5 seconds")

        # Si l'argument est -F
        if "-F" == argv[index]:

            # On récupère le nom du fichier dans lequel sauvegarder les
            # résultats si il y a eu un tournoi, si il n'y en a pas eu, cette
            # variable n'est juste jamais utilisée
            # Si le chemin est invalide, la sauvegarde échouera plus tard

            # On s'assure de plus qu'il existe un argument en plus, sinon une
            # exception sera levée
            if index + 1 < len(argv):
                arguments.filename = argv[index + 1]


    # On retourne la liste d'arguments
    return arguments

# Cette fonction affiche tous les paramètres disponibles
def printHelp():
    print("---------------------------------------------------------------------")
    print("Welcome to the best A.I. ever created! Here are your options to toy with it.")
    print("")
    print("-UI                  Enables the GUI")
    print("")
    print("-BDS [size]          Sets the size of the board, 10x10 by default")
    print("")
    print("-T [nb]              Allows tournaments to happen (nb is optional, sets the number of tournaments that should happen)")
    print("")
    print("-M [p1] [p2]         Sets a match that will happen between p1 and p2, which are the names of the players. If p1 or p2 is an incorrect name, the match will be cancelled")
    print("")
    print("-P                   Prints the list of available players")
    print("")
    print("-TM [time]           The maximum amount of time a player can spend looking for the best move to play")
    print("")
    print("-F [filename]        Saves the results of the tournament in this file")
    print("")
    print("-h                   Prints this very help")
    print("")
