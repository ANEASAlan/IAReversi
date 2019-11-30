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

    # On retourne la liste d'arguments
    return arguments
