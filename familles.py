from utils import nb_els_prec

famille      = 16
sous_famille = 14
rang = 0

taille_temp = 0

def get_rang(element):
    nb_uns = len(element.replace("0", ""))
    rang = 1
    for ind in range(len(element)):
        pos = len(element) - ind
        bit = element[ind]
        if bit == "1":
            bonds = pos - nb_uns
            som = nb_els_prec(nb_uns, bonds)
            # print(bit + " | bonds: " + str(pos) + " - " + str(nb_uns) + " = " + str(bonds) + " | somme: " + str(som))
            nb_uns -= 1
            rang += som

    return rang


nbEls = nb_els_prec(1, 0)
print("sommme: " + str(nbEls))
# exit()

r = get_rang("1011101111111111")
print("rang: " + str(r))
# exit()

for a in range(1, famille - sous_famille + 1):
    val = nb_els_prec(sous_famille, a)
    print(str(a) + " => " + str(val))


if sous_famille > famille:
    print("Le nombre de bits de la famille doit etre superieur a celui de la sous-famille")
    exit()

print("(" + str(famille) + ", " + str(sous_famille) + ")")

for el in range(2**famille):
    bin_num = '{0:b}'.format(el) # conversion decimal -> binaire
    uns_num = bin_num.replace("0", "") 
    if len(uns_num) == sous_famille:
        rang += 1
        taille_temp += 1
        bits = bin_num.zfill(famille)  # ajout des zeros au debut pour avoir toujours le meme nombre de bits
        print(bits + " | " + str(rang) + " | rang: " + str(get_rang(bits)))
        if len(bits.strip("0")) == sous_famille:
            print("===================== " + str(taille_temp) + " elements")
            taille_temp = 0
