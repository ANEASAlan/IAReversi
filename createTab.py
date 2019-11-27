def createTab(size, factor):
    finalTab = []

    expo = size//2-1
    j = 0
    tabOfTabs = []
    
    while j < size//2 :

        tab1 = []
        i = 0
        nb = factor ** (expo)

        while i < size//2:
            tab1.append(nb)
            if i < size//2-1 or size%2==0 :
                tab1.append(nb)
            if i < size//2-1 :
                nb = nb // factor
            i = i + 2


        i = size//2 + 1
        nb = nb * factor
        while i < size:
            tab1.append(nb)
            tab1.append(nb)
            nb = nb * factor
            i = i + 2

        tabOfTabs.append(tab1)
        expo = expo - 1
        j = j + 2

    print(tabOfTabs)

    ind = 0
    k = 0
    while k < size//2 :
        finalTab.append(tabOfTabs[ind])
        if k < size//2-1 or size%2==0 :
            finalTab.append(tabOfTabs[ind])
        k = k + 2
        ind = ind + 1

    k = size//2 + 1
    ind = size//4 - 1
    while k < size :
        finalTab.append(tabOfTabs[ind])
        finalTab.append(tabOfTabs[ind])
        k = k + 2
        ind = ind - 1

    return finalTab


    
finalTab = createTab(10, 3)
print(finalTab)


#reste plus qu'à mettre en négatif les valeurs négatives
