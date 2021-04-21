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
        # print(str(i) + " => " + nb1[i] + " + " + nb2[i] + " = " + str(rep) + " ("+ str(retenue) +")")
        resultat = str(rep) + resultat

    if retenue != 0:
        resultat = "1" + resultat

    return resultat