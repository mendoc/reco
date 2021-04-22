def nb_els_prec(nbu, n):
    if n < 1 or nbu < 1:
        return 0
    elif nbu == 1 :
        return n
    else:
        res = 1
        for i in range(nbu):
            res *= (n + i)/(i + 1)
        return int(res)

def add(nb1, nb2):
    if len(nb1) > len(nb2):
        while len(nb2) < len(nb1):
            nb2 = "0" + nb2
    else:
        while len(nb1) < len(nb2):
            nb1 = "0" + nb1

    retenue = 0
    resultat = ""
    for i in range(len(nb1)-1, -1, -1):
        rep = int(nb1[i]) + int(nb2[i])
        
        if retenue != 0:
            rep += retenue
            retenue = 0
        
        if rep > 9:
            retenue = 1
            rep = rep % 10
        resultat = str(rep) + resultat

    if retenue != 0:
        resultat = "1" + resultat

    return resultat

def mul(nb1, nb2):
    retenue = 0
    resultat = "0"
    lignes = []
    if len(nb1) < len(nb2):
        t = nb2
        nb2 = nb1
        nb1 = t
    
    for i in range(len(nb2)-1, -1, -1):
        ligne = ""
        for k in range(len(nb1)-1, -1, -1):
            prod = int(nb2[i]) * int(nb1[k])

            if retenue != 0:
                prod += retenue
                retenue = 0

            if prod > 9:
                retenue = int(prod / 10)
                prod = prod % 10
            
            ligne = str(prod) + ligne
            
            if k == 0 and retenue != 0:
                ligne = str(retenue) + ligne
                retenue = 0
        
        pad = len(ligne) + len(nb2) - i - 1
        while len(ligne) < pad:
            ligne += "0"
        
        resultat = add(resultat, ligne)
    
    return resultat

def sous(nb1, nb2):
    retenue = 0
    resultat = ""

    if len(nb1) < len(nb2):
        return "0"
    
    if len(nb1) > len(nb2):
        while len(nb2) < len(nb1):
            nb2 = "0" + nb2
    else:
        while len(nb1) < len(nb2):
            nb1 = "0" + nb1
    
    if nb1 < nb2:
        return "0"
    
    for i in range(len(nb1)-1, -1, -1):
        if retenue != 0:
            rep = int(nb1[i]) - (int(nb2[i]) + retenue)
            retenue = 0
        else:
            rep = int(nb1[i]) - int(nb2[i])

        if rep < 0:
            rep += 10
            retenue = 1
        
        if i != 0 or rep != 0:
            resultat = str(rep) + resultat
        
    return resultat

def sup(nb1, nb2):
    if len(nb1) > len(nb2):
        while len(nb2) < len(nb1):
            nb2 = "0" + nb2
    else:
        while len(nb1) < len(nb2):
            nb1 = "0" + nb1
    
    return nb1 > nb2

def sup_egal(nb1, nb2):
    if len(nb1) > len(nb2):
        while len(nb2) < len(nb1):
            nb2 = "0" + nb2
    else:
        while len(nb1) < len(nb2):
            nb1 = "0" + nb1
    
    return nb1 >= nb2

def div(nb1, nb2):
    resultat = ""
    rep = nb1
    
    if len(nb1) < len(nb2):
        return "0"
    
    # print(nb1)

    dividende = nb1
    quotient = ""
    portion = ""
    reste = ""
    for i in range(len(dividende)):
        portion += nb1[i]
        if sup_egal(portion, nb2):
            print(portion)
            facteur = "0"
            temp = portion
            while sup(temp, nb2):
                temp = sous(temp, nb2)
                facteur = add(facteur, "1")
            prod = mul(facteur, nb2)
            reste = sous(portion, prod)
            portion = reste.lstrip('0')
            resultat += facteur
            print("facteur:", facteur, "nb2:", nb2, "prod:", prod, "reste:", reste, "portion:", portion)
        print(portion)
    
    return resultat, reste.lstrip('0')

# res = div("500641876841681764684617684614646416604", "178518176876878171676788")
# # res, _ = div("25784", "87")
# print("resultat:", res)
# print(add(mul('284438181960', "178518176876878171676788"), '65734870560513411968604'))