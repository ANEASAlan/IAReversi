def createTab(factor, size = 10): #factor est le gradient logarithmique que l'on donnera aux cases (pour gradient = 3, les cases auront les valeurs 3, 9, 27 ou 81 à un signe près), size est la taille d'un côté de tableau carré (10 sur ce projet)
    finalTab = []   # tableau des Power Spots

    expo = size//2-1   # pour calculer le Power des coins selon la taille
    j = 0
    tabOfTabs = []  # étant donné que des lignes du tableau des Power Spots seront identiques, sans compter le signe des valeurs, je fais en premier lieu un tableau qui contiendra les lignes, pour je les y ajouterai plus tard

    # PARTIE 1 : Remplir le tableau qui contiendra les lignes à mettre dans le tableau de Power Spots
    
    while j < size//2 : # le tableau étant très symmétrique, je calcule seulement la partie haute

        tab1 = []
        nb = factor ** (expo)   # pour calculer le Power des coins selon l'exposant calculé plus tôt

        for i in range(0,size//2,2) :   # le tableau étant très symmétrique, je fais d'abord la partie haute gauche
            tab1.append(nb) # j'ajoute la valeur du Power calculée (la premiere étant celle du coin haut gauche, 81 pour size = 10 et factor = 3)
            if i < size//2-1 or size%2==0 : # si on est pas arrivé au-delà du milieu du board
                tab1.append(nb) # je le fais deux fois, car j'ai remarqué que si on applique notre façon d'assigner les power spots, on a à chaque fois deux fois la même valeur à la suite
            if i < size//2-1 :  # si on est pas arrivé au-delà du milieu du board
                nb = nb // factor  # ensuite on change la valeur à attribuer à la case
            

        nb = nb * factor
        for i in range(size//2 + 1,size,2) :   # le tableau étant très symmétrique, je fais ensuite la partie haute droite
            tab1.append(nb)
            tab1.append(nb)
            nb = nb * factor

        tabOfTabs.append(tab1)
        expo = expo - 1
        j = j + 2

    # PARTIE 2 : Remplir le tableau des Power Spots avec celui qui contient ses lignes

    ind = 0
    for k in range(0,size//2,2) :   # le tableau étant très symmétrique, je fais d'abord la partie haute
        tab1 = tabOfTabs[ind].copy()    # afin de pouvoir modifier certaines valeurs plus tard, je ne dois pas passer les tableaux par indices avec un append, je fais donc une copie
        finalTab.append(tab1)   # je mets ensuite la ligne voulue
        if k < size//2-1 or size%2==0 : # si on est pas arrivé au-delà du milieu du board
            tab2 = tabOfTabs[ind].copy()    # je le fais deux fois, car j'ai remarqué que si on applique notre façon d'assigner les power spots, on a à chaque fois deux fois la même ligne à la suite
            finalTab.append(tab2)
        ind = ind + 1

    ind = size//4 - 1
    for k in range(size//2 + 1,size,2) :    # le tableau étant très symmétrique, je fais ensuite la partie basse
        tab1 = tabOfTabs[ind].copy()
        finalTab.append(tab1)
        tab2 = tabOfTabs[ind].copy()
        finalTab.append(tab2)
        ind = ind - 1

    # PARTIE 3 : Mettre au négatif les valeurs qui devraient être négatives

    for y in range(1,size//2,2) :   # le tableau étant très symmétrique, je fais d'abord la partie haute, je dois mettre au négatif une ligne sur deux
        for x in range(0,size): # je dois mettre au négatif toute une ligne (ou colonne)
            #if finalTab[y][x] > 0:
            finalTab[y][x] = finalTab[y][x] * (-1)  # mettre la valeur au négatif

    for y in range(size-2,size//2,-2) : # le tableau étant très symmétrique, je fais ensuite la partie basse
        for x in range(0,size):
            #if finalTab[y][x] > 0:
            finalTab[y][x] = finalTab[y][x] * (-1)

    for x in range(1,size//2,2) :   # le tableau étant très symmétrique, je fais d'abord la partie gauche
        for y in range(0,size):
            if finalTab[y][x] > 0:
                finalTab[y][x] = finalTab[y][x] * (-1)

    for x in range(size-2,size//2,-2) : # le tableau étant très symmétrique, je fais ensuite la partie droite
        for y in range(0,size):
            if finalTab[y][x] > 0:
                finalTab[y][x] = finalTab[y][x] * (-1)

    return finalTab # le tableau est enfin fait, je peux donc le renvoyer


    
#finalTab = createTab(3) exemple d'appel de la fonction pour un facteur 3 et un tableau de 10x10
