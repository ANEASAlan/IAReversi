import Tournament
from xlwt import Workbook
import xlwt

# retourne l'index du joueur dans le tableau
def getPlayerIndex(players, player):
    i = 0
    for p in players:
        if p == player:
            return i
        i += 1
    return -1

# Cette fonction initialise la matrice passée en paramètre en fonction du
# nombre de joueur
def initMat(players, matrice):
    for x in range(len(players)):
        tmp = []
        for y in range(len(players)):
            tmp.append(0)
        matrice.append(tmp)

# Cette fonction rempli la matrcie en fonction des matchs qui ont été joués
# Une victoire ajoute un point, une défaite enlève un point
def fillMat(players, matchs, matrice):
    for match in matchs:
        # Si il n'y a pas eu de gagnants il n'y a rien à faire
        if match.winner != None:
            winner = getPlayerIndex(players, match.winner)
            loser = getPlayerIndex(players, match.loser)
            matrice[loser][winner] -= 1
            matrice[winner][loser] += 1

# Cette fonction sauvegarde les données stockés dans la matrice dans un fichier
# csv
def saveResults(filename, players, matrice):

    # On ouvre un book pour écrire dedans (c'est comme un fichier)
    book = Workbook()

    # On ajoute une feuille (il peut y en avoir plusieurs, il faut donc en
    # spécifier une)
    sheet = book.add_sheet('Sheet')

    # On écrit la liste des joueurs sur la première ligne (avec une cellule
    # vide tout à gauche)
    for x_index in range(len(players)):
        sheet.write(x_index + 1, 0, players[x_index].name)

    # On remplit les scores
    for y_index in range(len(players)):

        # On écrit le nom du joueur en premier sur la ligne
        sheet.write(0, y_index + 1, players[y_index].name)

        # On écrit ses résultats en fonction de ses adversaires
        for x_index in range(0, len(players)):

            # On choisit la couleur de fond (vert > 0, rouge < 0, bleu = 0)
            st = xlwt.easyxf('pattern: pattern solid;')
            if matrice[x_index][y_index] > 0:
                st.pattern.pattern_fore_colour = 3
            elif matrice[x_index][y_index] < 0:
                st.pattern.pattern_fore_colour = 2
            else:
                st.pattern.pattern_fore_colour = 4
            sheet.write(x_index + 1, y_index + 1, str(matrice[x_index][y_index]), st)

    # On sauvegarde le book en fichier
    book.save(filename)
